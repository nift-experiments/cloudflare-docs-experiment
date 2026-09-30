---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/encoding/
  description: Takes a stream of code points as input and emits a stream of bytes.
  full_title: Encoding · Cloudflare Workers docs
  head_html: <title>Encoding · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Takes a stream of code points as input and emits a stream of bytes."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/encoding/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/encoding/index.md"><meta property="og:title" content="Encoding · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Takes a stream of code points as input and emits a stream of bytes."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/encoding/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/encoding/#page","headline":"Encoding \u00b7 Cloudflare Workers docs","description":"Takes a stream of code points as input and emits a stream of bytes.","url":"https://developers.cloudflare.com/workers/runtime-apis/encoding/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/encoding/
  schema: 1
---
<h2 id="textencoder">TextEncoder</h2>
<h3 id="background">Background</h3>
<p>The <code>TextEncoder</code> takes a stream of code points as input and emits a stream of bytes. Encoding types passed to the constructor are ignored and a UTF-8 <code>TextEncoder</code> is created.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/TextEncoder"><code>TextEncoder()</code></a> returns a newly constructed <code>TextEncoder</code> that generates a byte stream with UTF-8 encoding. <code>TextEncoder</code> takes no parameters and throws no exceptions.</p>
<h3 id="constructor">Constructor</h3>
<pre tabindex="0"><code class="language-js">let encoder = new TextEncoder();&#10;</code></pre>
<h3 id="properties">Properties</h3>
<ul>
<li><code>encoder.encoding</code> DOMString read-only
<ul>
<li>The name of the encoder as a string describing the method the <code>TextEncoder</code> uses (always <code>utf-8</code>).</li>
</ul>
</li>
</ul>
<h3 id="methods">Methods</h3>
<ul>
<li>
<p><code>encode(inputUSVString)</code> : Uint8Array</p>
<ul>
<li>Encodes a string input.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="textdecoder">TextDecoder</h2>
<h3 id="background-1">Background</h3>
<p>The <code>TextDecoder</code> interface represents a UTF-8 decoder. Decoders take a stream of bytes as input and emit a stream of code points.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/TextDecoder"><code>TextDecoder()</code></a> returns a newly constructed <code>TextDecoder</code> that generates a code-point stream.</p>
<h3 id="constructor-1">Constructor</h3>
<pre tabindex="0"><code class="language-js">let decoder = new TextDecoder();&#10;</code></pre>
<h3 id="properties-1">Properties</h3>
<ul>
<li>
<p><code>decoder.encoding</code> DOMString read-only</p>
<ul>
<li>The name of the decoder that describes the method the <code>TextDecoder</code> uses.</li>
</ul>
</li>
<li>
<p><code>decoder.fatal</code> boolean read-only</p>
<ul>
<li>Indicates if the error mode is fatal.</li>
</ul>
</li>
<li>
<p><code>decoder.ignoreBOM</code> boolean read-only</p>
<ul>
<li>Indicates if the byte-order marker is ignored.</li>
</ul>
</li>
</ul>
<h3 id="methods-1">Methods</h3>
<ul>
<li><code>decode()</code> : DOMString
<ul>
<li>Decodes using the method specified in the <code>TextDecoder</code> object. Learn more at <a href="https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/decode">MDN’s <code>TextDecoder</code> documentation</a>.</li>
</ul>
</li>
</ul>
