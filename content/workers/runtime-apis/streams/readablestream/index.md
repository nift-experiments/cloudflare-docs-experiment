---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/
  description: Learn about the ReadableStream API for reading streamed data in Cloudflare Workers.
  full_title: ReadableStream · Cloudflare Workers docs
  head_html: <title>ReadableStream · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about the ReadableStream API for reading streamed data in Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/index.md"><meta property="og:title" content="ReadableStream · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about the ReadableStream API for reading streamed data in Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/#page","headline":"ReadableStream \u00b7 Cloudflare Workers docs","description":"Learn about the ReadableStream API for reading streamed data in Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/readablestream/
  schema: 1
---
<h2 id="background">Background</h2>
<p>A <code>ReadableStream</code> is returned by the <code>readable</code> property inside <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a>.</p>
<h2 id="properties">Properties</h2>
<ul>
<li><code>locked</code> boolean
<ul>
<li>A Boolean value that indicates if the readable stream is locked to a reader.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>pipeTo(destinationWritableStream, optionsPipeToOptions)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Pipes the readable stream to a given writable stream <code>destination</code> and returns a promise that is fulfilled when the <code>write</code> operation succeeds or rejects it if the operation fails.</li>
</ul>
</li>
<li>
<p><code>pipeThrough(transformStream, optionsPipeToOptions)</code> : ReadableStream</p>
<ul>
<li>Pipes the readable stream to the writable side of a given <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a> and returns the transform's readable side, so that calls can be chained. <code>options</code> accepts the same values as <code>pipeTo()</code>.</li>
</ul>
</li>
<li>
<p><code>getReader(optionsObject)</code> : ReadableStreamDefaultReader</p>
<ul>
<li>Gets an instance of <code>ReadableStreamDefaultReader</code> and locks the <code>ReadableStream</code> to that reader instance. This method accepts an object argument indicating options. The only supported option is <code>mode</code>, which can be set to <code>byob</code> to create a <a href="/workers/runtime-apis/streams/readablestreambyobreader/"><code>ReadableStreamBYOBReader</code></a>, as shown here:</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-js">let reader = readable.getReader({ mode: &#x27;byob&#x27; });&#10;</code></pre>
<ul>
<li>
<p><code>cancel(reasonstringoptional)</code> : Promise&lt;void&gt;</p>
<ul>
<li>Cancels the stream. <code>reason</code> is an optional human-readable string indicating the reason for cancellation. <code>reason</code> will be passed to the underlying source’s cancel algorithm. Any data not yet read is lost.</li>
</ul>
</li>
<li>
<p><code>tee()</code> : [ReadableStream, ReadableStream]</p>
<ul>
<li>Locks the stream and returns an array of two new <code>ReadableStream</code> instances, each of which reads the same data as the original stream. Backpressure to the underlying source follows the branch with the most unread data, which avoids unbounded buffering when one branch reads more slowly than the other, as long as the underlying source responds to backpressure. Refer to <a href="https://github.com/cloudflare/workerd/blob/main/src/workerd/api/streams/README.md#tee-behavior">workerd's streams documentation</a> for implementation details.</li>
</ul>
</li>
<li>
<p><code>values(optionsObject)</code> : AsyncIterableIterator</p>
<ul>
<li>Returns an async iterator that reads and consumes the chunks of the stream. This method accepts an object argument indicating options. The only supported option is <code>preventCancel</code>, which, when <code>true</code>, prevents the stream from being canceled when the iterator exits early (for example, from a <code>break</code> statement). A <code>ReadableStream</code> is also async iterable directly:</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17068.md")
</div>
<h3 id="pipetooptions"><code>PipeToOptions</code></h3>
<ul>
<li>
<p><code>preventClose</code> bool</p>
<ul>
<li>When <code>true</code>, closure of the source <code>ReadableStream</code> will not cause the destination <code>WritableStream</code> to be closed.</li>
</ul>
</li>
<li>
<p><code>preventAbort</code> bool</p>
<ul>
<li>When <code>true</code>, errors in the source <code>ReadableStream</code> will no longer abort the destination <code>WritableStream</code>. <code>pipeTo</code> will return a rejected promise with the error from the source or any error that occurred while aborting the destination.</li>
</ul>
</li>
</ul>
<h2 id="static-methods">Static methods</h2>
<ul>
<li>
<p><code>ReadableStream.from(asyncIterable)</code> : ReadableStream</p>
<ul>
<li>Creates a new <code>ReadableStream</code> whose chunks are the values yielded by <code>asyncIterable</code>, which may be any iterable or async iterable, including an async generator.</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17069.md")
</div>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#rs-model">Readable streams in the WHATWG Streams API specification</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream">MDN’s <code>ReadableStream</code> documentation</a></li>
</ul>
