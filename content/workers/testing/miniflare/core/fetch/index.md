---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/
  description: Dispatch and test HTTP fetch events in Miniflare for Cloudflare Workers.
  full_title: Fetch Events · Cloudflare Workers docs
  head_html: <title>Fetch Events · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Dispatch and test HTTP fetch events in Miniflare for Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/index.md"><meta property="og:title" content="Fetch Events · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Dispatch and test HTTP fetch events in Miniflare for Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/#page","headline":"Fetch Events \u00b7 Cloudflare Workers docs","description":"Dispatch and test HTTP fetch events in Miniflare for Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/core/fetch/
  schema: 1
---
<ul>
<li><a href="/workers/runtime-apis/handlers/fetch/"><code>FetchEvent</code> Reference</a></li>
</ul>
<h2 id="http-requests">HTTP Requests</h2>
<p>Whenever an HTTP request is made, a <code>Request</code> object is dispatched to your worker, then the generated <code>Response</code> is returned. The
<code>Request</code> object will include a
<a href="/workers/runtime-apis/request#incomingrequestcfproperties"><code>cf</code> object</a>.
Miniflare will log the method, path, status, and the time it took to respond.</p>
<p>If the Worker throws an error whilst generating a response, an error page
containing the stack trace is returned instead.</p>
<h2 id="dispatching-events">Dispatching Events</h2>
<p>When using the API, the <code>dispatchFetch</code> function can be used to dispatch <code>fetch</code>
events to your Worker. This can be used for testing responses. <code>dispatchFetch</code>
has the same API as the regular <code>fetch</code> method: it either takes a <code>Request</code>
object, or a URL and optional <code>RequestInit</code> object:</p>
<pre tabindex="0"><code class="language-js">import { Miniflare, Request } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      const body = JSON.stringify({&#10;        url: event.request.url,&#10;        header: event.request.headers.get(&quot;X-Message&quot;),&#10;      });&#10;      return new Response(body, {&#10;        headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;      });&#10;    })&#10;  }&#10;  `,&#10;});&#10;&#10;let res = await mf.dispatchFetch(&quot;http://localhost:8787/&quot;);&#10;console.log(await res.json()); // { url: &quot;http://localhost:8787/&quot;, header: null }&#10;&#10;res = await mf.dispatchFetch(&quot;http://localhost:8787/1&quot;, {&#10;	headers: { &quot;X-Message&quot;: &quot;1&quot; },&#10;});&#10;console.log(await res.json()); // { url: &quot;http://localhost:8787/1&quot;, header: &quot;1&quot; }&#10;&#10;res = await mf.dispatchFetch(&#10;	new Request(&quot;http://localhost:8787/2&quot;, {&#10;		headers: { &quot;X-Message&quot;: &quot;2&quot; },&#10;	}),&#10;);&#10;console.log(await res.json()); // { url: &quot;http://localhost:8787/2&quot;, header: &quot;2&quot; }&#10;</code></pre>
<p>When dispatching events, you are responsible for adding
<a href="/fundamentals/reference/http-headers/"><code>CF-*</code> headers</a> and the
<a href="/workers/runtime-apis/request#incomingrequestcfproperties"><code>cf</code> object</a>.
This lets you control their values for testing:</p>
<pre tabindex="0"><code class="language-js">const res = await mf.dispatchFetch(&quot;http://localhost:8787&quot;, {&#10;	headers: {&#10;		&quot;CF-IPCountry&quot;: &quot;GB&quot;,&#10;	},&#10;	cf: {&#10;		country: &quot;GB&quot;,&#10;	},&#10;});&#10;</code></pre>
<h2 id="upstream">Upstream</h2>
<p>Miniflare will call each <code>fetch</code> listener until a response is returned. If no
response is returned, or an exception is thrown and <code>passThroughOnException()</code>
has been called, the response will be fetched from the specified upstream
instead:</p>
<pre tabindex="0"><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	script: `&#10;  addEventListener(&quot;fetch&quot;, (event) =&gt; {&#10;    event.passThroughOnException();&#10;    throw new Error();&#10;  });&#10;  `,&#10;	upstream: &quot;https://miniflare.dev&quot;,&#10;});&#10;// If you don&#x27;t use the same upstream URL when dispatching, Miniflare will&#10;// rewrite it to match the upstream&#10;const res = await mf.dispatchFetch(&quot;https://miniflare.dev/core/fetch&quot;);&#10;console.log(await res.text()); // Source code of this page&#10;</code></pre>
