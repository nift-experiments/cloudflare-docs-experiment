---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/eventsource/
  description: EventSource is a server-sent event API that allows a server to push events to a client.
  full_title: EventSource · Cloudflare Workers docs
  head_html: <title>EventSource · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="EventSource is a server-sent event API that allows a server to push events to a client."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/eventsource/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/eventsource/index.md"><meta property="og:title" content="EventSource · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="EventSource is a server-sent event API that allows a server to push events to a client."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/eventsource/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/eventsource/#page","headline":"EventSource \u00b7 Cloudflare Workers docs","description":"EventSource is a server-sent event API that allows a server to push events to a client.","url":"https://developers.cloudflare.com/workers/runtime-apis/eventsource/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/eventsource/
  schema: 1
---
<h2 id="background">Background</h2>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/EventSource"><code>EventSource</code></a> interface is a server-sent event API that allows a server to push events to a client. The <code>EventSource</code> object is used to receive server-sent events. It connects to a server over HTTP and receives events in a text-based format.</p>
<h3 id="constructor">Constructor</h3>
<pre tabindex="0"><code class="language-js">let eventSource = new EventSource(url, options);&#10;</code></pre>
<ul>
<li><code>url</code> USVString - The URL to which to connect.</li>
<li><code>options</code> EventSourceInit - An optional dictionary containing any optional settings.</li>
</ul>
<p>By default, the <code>EventSource</code> will use the global <code>fetch()</code> function under the
covers to make requests. If you need to use a different fetch implementation as
provided by a Cloudflare Workers binding, you can pass the <code>fetcher</code> option:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(req, env) {&#10;    let eventSource = new EventSource(url, { fetcher: env.MYFETCHER });&#10;    // ...&#10;  }&#10;};&#10;</code></pre>
<p>Note that the <code>fetcher</code> option is a Cloudflare Workers specific extension.</p>
<h3 id="properties">Properties</h3>
<ul>
<li><code>eventSource.url</code> USVString read-only
<ul>
<li>The URL of the event source.</li>
</ul>
</li>
<li><code>eventSource.readyState</code> USVString read-only
<ul>
<li>The state of the connection.</li>
</ul>
</li>
<li><code>eventSource.withCredentials</code> Boolean read-only
<ul>
<li>A Boolean indicating whether the <code>EventSource</code> object was instantiated with cross-origin (CORS) credentials set (<code>true</code>), or not (<code>false</code>).</li>
</ul>
</li>
</ul>
<h3 id="methods">Methods</h3>
<ul>
<li><code>eventSource.close()</code>
<ul>
<li>Closes the connection.</li>
</ul>
</li>
<li><code>eventSource.onopen</code>
<ul>
<li>An event handler called when a connection is opened.</li>
</ul>
</li>
<li><code>eventSource.onmessage</code>
<ul>
<li>An event handler called when a message is received.</li>
</ul>
</li>
<li><code>eventSource.onerror</code>
<ul>
<li>An event handler called when an error occurs.</li>
</ul>
</li>
</ul>
<h3 id="events">Events</h3>
<ul>
<li><code>message</code>
<ul>
<li>Fired when a message is received.</li>
</ul>
</li>
<li><code>open</code>
<ul>
<li>Fired when the connection is opened.</li>
</ul>
</li>
<li><code>error</code>
<ul>
<li>Fired when an error occurs.</li>
</ul>
</li>
</ul>
<h3 id="class-methods">Class Methods</h3>
<ul>
<li><code>EventSource.from(readableStreamReadableStream) : EventSource</code>
<ul>
<li>This is a Cloudflare Workers specific extension that creates a new <code>EventSource</code> object from an existing <code>ReadableStream</code>. Such an instance does not initiate a new connection but instead attaches to the provided stream.</li>
</ul>
</li>
</ul>
