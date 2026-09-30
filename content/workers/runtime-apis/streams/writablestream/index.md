---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/
  description: Use the WritableStream API in Workers to write data to a stream destination.
  full_title: WritableStream · Cloudflare Workers docs
  head_html: <title>WritableStream · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the WritableStream API in Workers to write data to a stream destination."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/index.md"><meta property="og:title" content="WritableStream · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the WritableStream API in Workers to write data to a stream destination."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/#page","headline":"WritableStream \u00b7 Cloudflare Workers docs","description":"Use the WritableStream API in Workers to write data to a stream destination.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/writablestream/
  schema: 1
---
<h2 id="background">Background</h2>
<p>A <code>WritableStream</code> is the <code>writable</code> property of a <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a>. On the Workers platform, <code>WritableStream</code> cannot be directly created using the <code>WritableStream</code> constructor.</p>
<p>A typical way to write to a <code>WritableStream</code> is to pipe a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a> to it.</p>
<pre tabindex="0"><code class="language-js">readableStream&#10;  .pipeTo(writableStream)&#10;  .then(() =&gt; console.log(&#x27;All data successfully written!&#x27;))&#10;  .catch(e =&gt; console.error(&#x27;Something went wrong!&#x27;, e));&#10;</code></pre>
<p>To write to a <code>WritableStream</code> directly, you must use its writer.</p>
<pre tabindex="0"><code class="language-js">const writer = writableStream.getWriter();&#10;writer.write(data);&#10;</code></pre>
<p>Refer to the <a href="/workers/runtime-apis/streams/writablestreamdefaultwriter/">WritableStreamDefaultWriter</a> documentation for further detail.</p>
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>locked</code> boolean</p>
<ul>
<li>A Boolean value to indicate if the writable stream is locked to a writer.</li>
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
@markup("md", "content/.markup/bodies/17065.md")
</aside>
<ul>
<li>
<p><code>getWriter()</code> : WritableStreamDefaultWriter</p>
<ul>
<li>Gets an instance of <code>WritableStreamDefaultWriter</code> and locks the <code>WritableStream</code> to that writer instance.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#ws-model">Writable streams in the WHATWG Streams API specification</a></li>
</ul>
