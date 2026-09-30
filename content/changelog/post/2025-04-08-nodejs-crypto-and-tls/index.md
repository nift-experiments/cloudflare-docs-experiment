---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/
  description: New updates and improvements at Cloudflare.
  full_title: Improved support for Node.js Crypto and TLS APIs in Workers · Changelog
  head_html: <title>Improved support for Node.js Crypto and TLS APIs in Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Improved support for Node.js Crypto and TLS APIs in Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/#page","headline":"Improved support for Node.js Crypto and TLS APIs in Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-04-08-nodejs-crypto-and-tls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-04-08-nodejs-crypto-and-tls/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 8, 2025</time><h2 id="post-title">Improved support for Node.js Crypto and TLS APIs in Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled,
the following Node.js APIs are now available:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code></a></li>
</ul>
<p>This make it easier to reuse existing Node.js code in Workers or use npm packages that depend on these APIs.</p>
<h4 id="node-crypto">node:crypto</h4>
<p>The full <a href="https://nodejs.org/api/crypto.html"><code>node:crypto</code></a> API is now available in Workers.</p>
<p>You can use it to verify and sign data:</p>
<pre tabindex="0"><code class="language-js">import { sign, verify } from &quot;node:crypto&quot;;&#10;&#10;const signature = sign(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PRIVATE_KEY);&#10;const verified = verify(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PUBLIC_KEY, signature);&#10;</code></pre>
<p>Or, to encrypt and decrypt data:</p>
<pre tabindex="0"><code class="language-js">import { publicEncrypt, privateDecrypt } from &quot;node:crypto&quot;;&#10;&#10;const encrypted = publicEncrypt(env.PUBLIC_KEY, &quot;some data&quot;);&#10;const plaintext = privateDecrypt(env.PRIVATE_KEY, encrypted);&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code> documentation</a> for more information.</p>
<h4 id="node-tls">node:tls</h4>
<p>The following APIs from <code>node:tls</code> are now available:</p>
<ul>
<li><a href="https://nodejs.org/api/tls.html#tlsconnectoptions-callback"><code>connect</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#class-tlstlssocket"><code>TLSSocket</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert"><code>checkServerIdentity</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions"><code>createSecureContext</code></a></li>
</ul>
<p>This enables secure connections over TLS (Transport Layer Security) to external services.</p>
<pre tabindex="0"><code class="language-js">import { connect } from &quot;node:tls&quot;;&#10;&#10;// ... in a request handler ...&#10;const connectionOptions = { key: env.KEY, cert: env.CERT };&#10;const socket = connect(url, connectionOptions, () =&gt; {&#10;	if (socket.authorized) {&#10;		console.log(&quot;Connection authorized&quot;);&#10;	}&#10;});&#10;&#10;socket.on(&quot;data&quot;, (data) =&gt; {&#10;	console.log(data);&#10;});&#10;&#10;socket.on(&quot;end&quot;, () =&gt; {&#10;	console.log(&quot;server ends connection&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code> documentation</a> for more information.</p>
</div></article></div>
