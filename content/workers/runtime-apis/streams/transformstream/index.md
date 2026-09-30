---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/
  description: Use the TransformStream API in Workers to pipe data between readable and writable streams.
  full_title: TransformStream · Cloudflare Workers docs
  head_html: <title>TransformStream · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the TransformStream API in Workers to pipe data between readable and writable streams."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/index.md"><meta property="og:title" content="TransformStream · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the TransformStream API in Workers to pipe data between readable and writable streams."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/#page","headline":"TransformStream \u00b7 Cloudflare Workers docs","description":"Use the TransformStream API in Workers to pipe data between readable and writable streams.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/transformstream/
  schema: 1
---
<h2 id="background">Background</h2>
<p>A transform stream consists of a pair of streams: a writable stream, known as its writable side, and a readable stream, known as its readable side. Writes to the writable side result in new data being made available for reading from the readable side.</p>
<p>Workers currently only implements an identity transform stream, a type of transform stream which forwards all chunks written to its writable side to its readable side, without any changes.</p>
<hr />
<h2 id="constructor">Constructor</h2>
<pre tabindex="0"><code class="language-js">let { readable, writable } = new TransformStream();&#10;</code></pre>
<ul>
<li>
<p><code>TransformStream()</code> TransformStream</p>
<ul>
<li>Returns a new identity transform stream.</li>
</ul>
</li>
</ul>
<h2 id="properties">Properties</h2>
<ul>
<li><code>readable</code> ReadableStream
<ul>
<li>An instance of a <code>ReadableStream</code>.</li>
</ul>
</li>
<li><code>writable</code> WritableStream
<ul>
<li>An instance of a <code>WritableStream</code>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="identitytransformstream"><code>IdentityTransformStream</code></h2>
<p>The current implementation of <code>TransformStream</code> in the Workers platform is not current compliant with the <a href="https://streams.spec.whatwg.org/#transform-stream">Streams Standard</a> and we will soon be making changes to the implementation to make it conform with the specification. In preparation for doing so, we have introduced the <code>IdentityTransformStream</code> class that implements behavior identical to the current <code>TransformStream</code> class. This type of stream forwards all chunks of byte data (in the form of <code>TypedArray</code>s) written to its writable side to its readable side, without any changes.</p>
<p>The <code>IdentityTransformStream</code> readable side supports <a href="https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamBYOBReader">bring your own buffer (BYOB) reads</a>.</p>
<h3 id="constructor-1">Constructor</h3>
<pre tabindex="0"><code class="language-js">let { readable, writable } = new IdentityTransformStream();&#10;</code></pre>
<ul>
<li>
<p><code>IdentityTransformStream()</code> IdentityTransformStream</p>
<ul>
<li>Returns a new identity transform stream.</li>
</ul>
</li>
</ul>
<h3 id="properties-1">Properties</h3>
<ul>
<li><code>readable</code> ReadableStream
<ul>
<li>An instance of a <code>ReadableStream</code>.</li>
</ul>
</li>
<li><code>writable</code> WritableStream
<ul>
<li>An instance of a <code>WritableStream</code>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="fixedlengthstream"><code>FixedLengthStream</code></h2>
<p>The <code>FixedLengthStream</code> is a specialization of <code>IdentityTransformStream</code> that limits the total number of bytes that the stream will passthrough. It is useful primarily because, when using <code>FixedLengthStream</code> to produce either a <code>Response</code> or <code>Request</code>, the fixed length of the stream will be used as the <code>Content-Length</code> header value as opposed to use chunked encoding when using any other type of stream. An error will occur if too many, or too few bytes are written through the stream.</p>
<h3 id="constructor-2">Constructor</h3>
<pre tabindex="0"><code class="language-js">let { readable, writable } = new FixedLengthStream(1000);&#10;</code></pre>
<ul>
<li>
<p><code>FixedLengthStream(length)</code> FixedLengthStream</p>
<ul>
<li>Returns a new identity transform stream.</li>
<li><code>length</code> maybe a <code>number</code> or <code>bigint</code> with a maximum value of <code>2^53 - 1</code>.</li>
</ul>
</li>
</ul>
<h3 id="properties-2">Properties</h3>
<ul>
<li><code>readable</code> ReadableStream
<ul>
<li>An instance of a <code>ReadableStream</code>.</li>
</ul>
</li>
<li><code>writable</code> WritableStream
<ul>
<li>An instance of a <code>WritableStream</code>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#transform-stream">Transform Streams in the WHATWG Streams API specification</a></li>
</ul>
