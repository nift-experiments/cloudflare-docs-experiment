---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/
  description: Handle incoming HTTP requests in Cloudflare Workers using the fetch() handler and return responses.
  full_title: Fetch Handler · Cloudflare Workers docs
  head_html: <title>Fetch Handler · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Handle incoming HTTP requests in Cloudflare Workers using the fetch() handler and return responses."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/index.md"><meta property="og:title" content="Fetch Handler · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Handle incoming HTTP requests in Cloudflare Workers using the fetch() handler and return responses."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/#page","headline":"Fetch Handler \u00b7 Cloudflare Workers docs","description":"Handle incoming HTTP requests in Cloudflare Workers using the fetch() handler and return responses.","url":"https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/handlers/fetch/
  schema: 1
---
<h2 id="background">Background</h2>
<p>Incoming HTTP requests to a Worker are passed to the <code>fetch()</code> handler as a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object. To respond to the request with a response, return a <a href="/workers/runtime-apis/response/"><code>Response</code></a> object:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&#x27;Hello World!&#x27;);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17178.md")
</aside>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>request</code> Request</p>
<ul>
<li>The incoming HTTP request.</li>
</ul>
</li>
<li>
<p><code>env</code> object</p>
<ul>
<li>The <a href="/workers/runtime-apis/bindings/">bindings</a> available to the Worker. As long as the <a href="/workers/wrangler/environments/">environment</a> has not changed, the same object (equal by identity) may be passed to multiple requests. You can also <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">import <code>env</code> from <code>cloudflare:workers</code></a> to access bindings from anywhere in your code.</li>
</ul>
</li>
<li>
<p><code>ctx.waitUntil(promisePromise)</code> : void</p>
<ul>
<li>Refer to <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a>.</li>
</ul>
</li>
<li>
<p><code>ctx.passThroughOnException()</code> : void</p>
<ul>
<li>Refer to <a href="/workers/runtime-apis/context/#passthroughonexception"><code>passThroughOnException</code></a>.</li>
</ul>
</li>
</ul>
