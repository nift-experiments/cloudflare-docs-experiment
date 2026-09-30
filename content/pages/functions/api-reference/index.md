---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/api-reference/
  description: Learn about the APIs used within Pages Functions.
  full_title: API reference · Cloudflare Pages docs
  head_html: <title>API reference · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about the APIs used within Pages Functions."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/api-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/api-reference/index.md"><meta property="og:title" content="API reference · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about the APIs used within Pages Functions."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/api-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/api-reference/#page","headline":"API reference \u00b7 Cloudflare Pages docs","description":"Learn about the APIs used within Pages Functions.","url":"https://developers.cloudflare.com/pages/functions/api-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/api-reference/
  schema: 1
---
<p>The following methods can be used to configure your Pages Function.</p>
<h2 id="methods">Methods</h2>
<h3 id="onrequests"><code>onRequests</code></h3>
<p>The <code>onRequest</code> method will be called unless a more specific <code>onRequestVerb</code> method is exported. For example, if both <code>onRequest</code> and <code>onRequestGet</code> are exported, only <code>onRequestGet</code> will be called for <code>GET</code> requests.</p>
<ul>
<li>
<p><code>onRequest(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all requests no matter what the request method is, as long as no specific request verb (like one of the methods below) is exported.</li>
</ul>
</li>
<li>
<p><code>onRequestGet(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>GET</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestPost(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>POST</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestPatch(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>PATCH</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestPut(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>PUT</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestDelete(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>DELETE</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestHead(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>HEAD</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestOptions(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>OPTIONS</code> requests.</li>
</ul>
</li>
</ul>
<h3 id="env-assets-fetch"><code>env.ASSETS.fetch()</code></h3>
<p>The <code>env.ASSETS.fetch()</code> function allows you to fetch a static asset from your Pages project.</p>
<p>You can pass a <a href="/workers/runtime-apis/request/">Request object</a>, URL string, or URL object to <code>env.ASSETS.fetch()</code> function. The URL must be to the pretty path, not directly to the asset. For example, if you had the path <code>/users/index.html</code>, you will request <code>/users/</code> instead of <code>/users/index.html</code>. This method call will run the header and redirect rules, modifying the response that is returned.</p>
<h2 id="types">Types</h2>
<h3 id="eventcontext"><code>EventContext</code></h3>
<p>The following are the properties on the <code>context</code> object which are passed through on the <code>onRequest</code> methods:</p>
<ul>
<li>
<p><code>request</code> <a href="/workers/runtime-apis/request/">Request</a></p>
<p>This is the incoming <a href="/workers/runtime-apis/request/">Request</a>.</p>
</li>
<li>
<p><code>functionPath</code> string</p>
<p>This is the path of the request.</p>
</li>
<li>
<p><code>waitUntil(promisePromise&lt;any&gt;)</code> void</p>
<p>Refer to <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code> documentation</a> for more information.</p>
</li>
<li>
<p><code>passThroughOnException()</code> void</p>
<p>Refer to <a href="/workers/runtime-apis/context/#passthroughonexception"><code>passThroughOnException</code> documentation</a> for more information. Note that this will not work on an <a href="/pages/functions/advanced-mode/">advanced mode project</a>.</p>
</li>
<li>
<p><code>next(input?Request | string, init?RequestInit)</code> Promise&lt;Response&gt;</p>
<p>Passes the request through to the next Function or to the asset server if no other Function is available.</p>
</li>
<li>
<p><code>env</code> <a href="#envwithfetch">EnvWithFetch</a></p>
</li>
<li>
<p><code>params</code> Params&lt;P&gt;</p>
<p>Holds the values from <a href="/pages/functions/routing/#dynamic-routes">dynamic routing</a>.</p>
<p>In the following example, you have a dynamic path that is <code>/users/[user].js</code>. When you visit the site on <code>/users/nevi</code> the <code>params</code> object would look like:</p>
</li>
</ul>
<pre tabindex="0"><code class="language-js">{&#10;	user: &quot;nevi&quot;;&#10;}&#10;</code></pre>
<p>This allows you fetch the dynamic value from the path:</p>
<pre tabindex="0"><code class="language-js">export function onRequest(context) {&#10;	return new Response(`Hello ${context.params.user}`);&#10;}&#10;</code></pre>
<p>Which would return <code>&quot;Hello nevi&quot;</code>.</p>
<ul>
<li><code>data</code> Data</li>
</ul>
<h3 id="envwithfetch"><code>EnvWithFetch</code></h3>
<p>Holds the environment variables, secrets, and bindings for a Function. This also holds the <code>ASSETS</code> binding which is how you can fallback to the asset-serving behavior.</p>
