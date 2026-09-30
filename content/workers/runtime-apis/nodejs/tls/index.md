---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/
  description: Use the Node.js tls module in Cloudflare Workers to create secure TLS connections to external services.
  full_title: tls · Cloudflare Workers docs
  head_html: <title>tls · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js tls module in Cloudflare Workers to create secure TLS connections to external services."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/index.md"><meta property="og:title" content="tls · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js tls module in Cloudflare Workers to create secure TLS connections to external services."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/#page","headline":"tls \u00b7 Cloudflare Workers docs","description":"Use the Node.js tls module in Cloudflare Workers to create secure TLS connections to external services.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/tls/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17130.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/tls.html"><code>node:tls</code></a> to create secure connections to
external services using <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security">TLS</a> (Transport Layer Security).</p>
<pre tabindex="0"><code class="language-js">import { connect } from &quot;node:tls&quot;;&#10;&#10;// ... in a request handler ...&#10;const connectionOptions = { key: env.KEY, cert: env.CERT };&#10;const socket = connect(url, connectionOptions, () =&gt; {&#10;	if (socket.authorized) {&#10;		console.log(&quot;Connection authorized&quot;);&#10;	}&#10;});&#10;&#10;socket.on(&quot;data&quot;, (data) =&gt; {&#10;	console.log(data);&#10;});&#10;&#10;socket.on(&quot;end&quot;, () =&gt; {&#10;	console.log(&quot;server ends connection&quot;);&#10;});&#10;</code></pre>
<p>The following APIs are available:</p>
<ul>
<li><a href="https://nodejs.org/api/tls.html#tlsconnectoptions-callback"><code>connect</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#class-tlstlssocket"><code>TLSSocket</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert"><code>checkServerIdentity</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions"><code>createSecureContext</code></a></li>
</ul>
<p>All other APIs, including <a href="https://nodejs.org/api/tls.html#class-tlsserver"><code>tls.Server</code></a> and <a href="https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener"><code>tls.createServer</code></a>,
are not supported and will throw a <code>Not implemented</code> error when called.</p>
<p>The full <code>node:tls</code> API is documented in the <a href="https://nodejs.org/api/tls.html">Node.js documentation for <code>node:tls</code></a>.</p>
