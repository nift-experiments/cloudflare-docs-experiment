---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/
  description: Use WritableStreamDefaultWriter in Workers to write data directly to a WritableStream.
  full_title: WritableStreamDefaultWriter · Cloudflare Workers docs
  head_html: <title>WritableStreamDefaultWriter · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use WritableStreamDefaultWriter in Workers to write data directly to a WritableStream."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/index.md"><meta property="og:title" content="WritableStreamDefaultWriter · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use WritableStreamDefaultWriter in Workers to write data directly to a WritableStream."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/#page","headline":"WritableStreamDefaultWriter \u00b7 Cloudflare Workers docs","description":"Use WritableStreamDefaultWriter in Workers to write data directly to a WritableStream.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/writablestreamdefaultwriter/
  schema: 1
---
<h2 id="background">Background</h2>
<p>A writer is used when you want to write directly to a <a href="/workers/runtime-apis/streams/writablestream/"><code>WritableStream</code></a>, rather than piping data to it from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>. For example:</p>
<pre tabindex="0"><code class="language-js">function writeArrayToStream(array, writableStream) {&#10;  const writer = writableStream.getWriter();&#10;  array.forEach(chunk =&gt; writer.write(chunk).catch(() =&gt; {}));&#10;&#10;  return writer.close();&#10;}&#10;&#10;writeArrayToStream([1, 2, 3, 4, 5], writableStream)&#10;  .then(() =&gt; console.log(&#x27;All done!&#x27;))&#10;  .catch(e =&gt; console.error(&#x27;Error with the stream: &#x27; + e));&#10;</code></pre>
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>writer.desiredSize</code> int</p>
<ul>
<li>The size needed to fill the stream’s internal queue, as an integer. Always returns 1, 0 (if the stream is closed), or <code>null</code> (if the stream has errors).</li>
</ul>
</li>
<li>
<p><code>writer.closed</code> Promise&lt;void&gt;</p>
<ul>
<li>A promise that indicates if the writer is closed. The promise is fulfilled when the writer stream is closed and rejected if there is an error in the stream.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>abort(reasonstringoptional)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Aborts the stream. This method returns a promise that fulfills with a response <code>undefined</code>. <code>reason</code> is an optional human-readable string indicating the reason for cancellation. <code>reason</code> will be passed to the underlying sink’s abort algorithm. If this writable stream is one side of a <a href="/workers/runtime-apis/streams/transformstream/">TransformStream</a>, then its abort algorithm causes the transform’s readable side to become errored with <code>reason</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17064.md")
</aside>
<ul>
<li>
<p><code>close()</code> : Promise&lt;void&gt;</p>
<ul>
<li>Attempts to close the writer. Remaining writes finish processing before the writer is closed. This method returns a promise fulfilled with <code>undefined</code> if the writer successfully closes and processes the remaining writes, or rejected on any error.</li>
</ul>
</li>
<li>
<p><code>releaseLock()</code> : void</p>
<ul>
<li>Releases the writer’s lock on the stream. Once released, the writer is no longer active. You can call this method before all pending <code>write(chunk)</code> calls are resolved. This allows you to queue a <code>write</code> operation, release the lock, and begin piping into the writable stream from another source, as shown in the example below.</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-js">let writer = writable.getWriter();&#10;// Write a preamble.&#10;writer.write(new TextEncoder().encode(&#x27;foo bar&#x27;));&#10;// While that’s still writing, pipe the rest of the body from somewhere else.&#10;writer.releaseLock();&#10;await someResponse.body.pipeTo(writable);&#10;</code></pre>
<ul>
<li>
<p><code>write(chunkany)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Writes a chunk of data to the writer and returns a promise that resolves if the operation succeeds.</li>
<li>The underlying stream may accept fewer kinds of type than <code>any</code>, it will throw an exception when encountering an unexpected type.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#ws-model">Writable streams in the WHATWG Streams API specification</a></li>
</ul>
