---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/
  description: New updates and improvements at Cloudflare.
  full_title: MessageChannel and MessagePort · Changelog
  head_html: <title>MessageChannel and MessagePort · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="MessageChannel and MessagePort · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/#page","headline":"MessageChannel and MessagePort \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-11-messagechannel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-11-messagechannel/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 11, 2025</time><h2 id="post-title">MessageChannel and MessagePort</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>A minimal implementation of the <a href="https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel">MessageChannel API</a> is now available in Workers. This means that you can use <code>MessageChannel</code> to send messages between different parts of your Worker, but not across different Workers.</p>
<p>The <code>MessageChannel</code> and <code>MessagePort</code> APIs will be available by default at the global scope
with any worker using a compatibility date of <code>2025-08-15</code> or later. It is also available
using the <code>expose_global_message_channel</code> compatibility flag, or can be explicitly disabled
using the <code>no_expose_global_message_channel</code> compatibility flag.</p>
<pre tabindex="0"><code class="language-js">const { port1, port2 } = new MessageChannel();&#10;&#10;port2.onmessage = (event) =&gt; {&#10;	console.log(&#x27;Received message:&#x27;, event.data);&#10;};&#10;&#10;port2.postMessage(&#x27;Hello from port2!&#x27;);&#10;</code></pre>
<p>Any value that can be used with the <code>structuredClone(...)</code> API can be sent over the port.</p>
<h4 id="differences">Differences</h4>
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
</div></article></div>
