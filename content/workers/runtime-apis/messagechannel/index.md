---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/messagechannel/
  description: Channel messaging with MessageChannel and MessagePort
  full_title: MessageChannel · Cloudflare Workers docs
  head_html: <title>MessageChannel · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Channel messaging with MessageChannel and MessagePort"><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/messagechannel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/messagechannel/index.md"><meta property="og:title" content="MessageChannel · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Channel messaging with MessageChannel and MessagePort"><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/messagechannel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/messagechannel/#page","headline":"MessageChannel \u00b7 Cloudflare Workers docs","description":"Channel messaging with MessageChannel and MessagePort","url":"https://developers.cloudflare.com/workers/runtime-apis/messagechannel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/messagechannel/
  schema: 1
---
<h2 id="background">Background</h2>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel">MessageChannel API</a> provides a way to create a communication channel between different parts of your application.</p>
<p>The Workers runtime provides a minimal implementation of the <code>MessageChannel</code> API that is
currently limited to uses with a single Worker instance. This means that you can use <code>MessageChannel</code> to send messages between different parts of your Worker, but not across different Workers.</p>
<pre tabindex="0"><code class="language-js">const { port1, port2 } = new MessageChannel();&#10;&#10;port2.onmessage = (event) =&gt; {&#10;	console.log(&#x27;Received message:&#x27;, event.data);&#10;};&#10;&#10;port2.postMessage(&#x27;Hello from port2!&#x27;);&#10;</code></pre>
<p>Any value that can be used with the <code>structuredClone(...)</code> API can be sent over the port.</p>
<h2 id="differences">Differences</h2>
<p>There are a number of key limitations to the <code>MessageChannel</code> API in Workers:</p>
<ul>
<li>Transfer lists are currently not supported. This means that you will not be able to transfer
ownership of objects like <code>ArrayBuffer</code> or <code>MessagePort</code> between ports.</li>
<li>The <code>MessagePort</code> is not yet serializable. This means that you cannot send a <code>MessagePort</code> object
through the <code>postMessage</code> method or via JSRPC calls.</li>
<li>The <code>'messageerror'</code> event is only partially supported. If the <code>'onmessage'</code> handler throws an
error, the <code>'messageerror'</code> event will be triggered, however, it will not be triggered when there
are errors serializing or deserializing the message data. Instead, the error will be thrown when
the <code>postMessage</code> method is called on the sending port.</li>
<li>The <code>'close'</code> event will be emitted on both ports when one of the ports is closed, however it
will not be emitted when the Worker is terminated or when one of the ports is garbage collected.</li>
</ul>
