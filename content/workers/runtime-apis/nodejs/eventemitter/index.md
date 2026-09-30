---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/
  description: Use the Node.js EventEmitter API in Cloudflare Workers to emit and listen for named events.
  full_title: EventEmitter · Cloudflare Workers docs
  head_html: <title>EventEmitter · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js EventEmitter API in Cloudflare Workers to emit and listen for named events."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/index.md"><meta property="og:title" content="EventEmitter · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js EventEmitter API in Cloudflare Workers to emit and listen for named events."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/#page","headline":"EventEmitter \u00b7 Cloudflare Workers docs","description":"Use the Node.js EventEmitter API in Cloudflare Workers to emit and listen for named events.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/eventemitter/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17162.md")
</aside>
<p>An <a href="https://nodejs.org/docs/latest/api/events.html#class-eventemitter"><code>EventEmitter</code></a>
is an object that emits named events that cause listeners to be called.</p>
<pre tabindex="0"><code class="language-js">import { EventEmitter } from &quot;node:events&quot;;&#10;&#10;const emitter = new EventEmitter();&#10;emitter.on(&quot;hello&quot;, (...args) =&gt; {&#10;	console.log(...args); // 1 2 3&#10;});&#10;&#10;emitter.emit(&quot;hello&quot;, 1, 2, 3);&#10;</code></pre>
<p>The implementation in the Workers runtime supports the entire Node.js <code>EventEmitter</code> API. This includes the <a href="https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises"><code>captureRejections</code></a>
option that allows improved handling of async functions as event handlers:</p>
<pre tabindex="0"><code class="language-js">const emitter = new EventEmitter({ captureRejections: true });&#10;emitter.on(&quot;hello&quot;, async (...args) =&gt; {&#10;	throw new Error(&quot;boom&quot;);&#10;});&#10;emitter.on(&quot;error&quot;, (err) =&gt; {&#10;	// the async promise rejection is emitted here!&#10;});&#10;</code></pre>
<p>Like Node.js, when an <code>'error'</code> event is emitted on an <code>EventEmitter</code> and there
is no listener for it, the error will be immediately thrown. However, in Node.js
it is possible to add a handler on the <code>process</code> object for the
<code>'uncaughtException'</code> event to catch globally uncaught exceptions. The
<code>'uncaughtException'</code> event, however, is currently not implemented in the
Workers runtime. It is strongly recommended to always add an <code>'error'</code> listener
to any <code>EventEmitter</code> instance.</p>
<p>Refer to the <a href="https://nodejs.org/api/events.html#class-eventemitter">Node.js documentation for <code>EventEmitter</code></a> for more information.</p>
