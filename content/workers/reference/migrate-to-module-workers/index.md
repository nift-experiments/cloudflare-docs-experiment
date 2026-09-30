---
cp9:
  canonical: https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/
  description: Write your Worker code in ES modules syntax for an optimized experience.
  full_title: Migrate from Service Workers to ES Modules · Cloudflare Workers docs
  head_html: <title>Migrate from Service Workers to ES Modules · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Write your Worker code in ES modules syntax for an optimized experience."><link rel="canonical" href="https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/index.md"><meta property="og:title" content="Migrate from Service Workers to ES Modules · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write your Worker code in ES modules syntax for an optimized experience."><meta property="og:url" content="https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/#page","headline":"Migrate from Service Workers to ES Modules \u00b7 Cloudflare Workers docs","description":"Write your Worker code in ES modules syntax for an optimized experience.","url":"https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/reference/migrate-to-module-workers/
  schema: 1
---
<p>This guide will show you how to migrate your Workers from the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API">Service Worker</a> format to the <a href="https://blog.cloudflare.com/workers-javascript-modules/">ES modules</a> format.</p>
<h2 id="advantages-of-migrating">Advantages of migrating</h2>
<p>There are several reasons to migrate your Workers to the ES modules format:</p>
<ol>
<li>Your Worker will run faster. With service workers, bindings are exposed as globals. This means that for every request, the Workers runtime must create a new JavaScript execution context, which adds overhead and time. Workers written using ES modules can reuse the same execution context across multiple requests.</li>
<li>Implementing <a href="/durable-objects/">Durable Objects</a> requires Workers that use ES modules.</li>
<li>Bindings for <a href="/d1/">D1</a>, <a href="/workers-ai/">Workers AI</a>, <a href="/vectorize/">Vectorize</a>, <a href="/workflows/">Workflows</a>, and <a href="/images/optimization/binding/">Images</a> can only be used from Workers that use ES modules.</li>
<li>You can <a href="/workers/versions-and-deployments/gradual-deployments/">gradually deploy changes to your Worker</a> when you use the ES modules format.</li>
<li>You can easily publish Workers using ES modules to <code>npm</code>, allowing you to import and reuse Workers within your codebase.</li>
</ol>
<h2 id="migrate-a-worker">Migrate a Worker</h2>
<p>The following example demonstrates a Worker that redirects all incoming requests to a URL with a <code>301</code> status code.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="service-workers-are-deprecated">Service Workers are deprecated</h3>
@markup("md", "content/.markup/bodies/16174.md")
</aside>
<p>With the Service Worker syntax, the example Worker looks like:</p>
<pre tabindex="0"><code class="language-js">async function handler(request) {&#10;  const base = &#x27;https://example.com&#x27;;&#10;  const statusCode = 301;&#10;&#10;  const destination = new URL(request.url, base);&#10;  return Response.redirect(destination.toString(), statusCode);&#10;}&#10;&#10;// Initialize Worker&#10;addEventListener(&#x27;fetch&#x27;, event =&gt; {&#10;  event.respondWith(handler(event.request));&#10;});&#10;</code></pre>
<p>Workers using ES modules format replace the <code>addEventListener</code> syntax with an object definition, which must be the file's default export (via <code>export default</code>). The previous example code becomes:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  fetch(request) {&#10;    const base = &quot;https://example.com&quot;;&#10;    const statusCode = 301;&#10;&#10;    const source = new URL(request.url);&#10;    const destination = new URL(source.pathname, base);&#10;    return Response.redirect(destination.toString(), statusCode);&#10;  },&#10;};&#10;</code></pre>
<h2 id="bindings">Bindings</h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to interact with resources on the Cloudflare developer platform.</p>
<p>Workers using ES modules format do not rely on any global bindings. However, Service Worker syntax accesses bindings on the global scope.</p>
<p>To understand bindings, refer the following <code>TODO</code> KV namespace binding example. To create a <code>TODO</code> KV namespace binding, you will:</p>
<ol>
<li>Create a KV namespace named <code>My Tasks</code> and receive an ID that you will use in your binding.</li>
<li>Create a Worker.</li>
<li>Find your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> and add a KV namespace binding:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16175.md")
</div>
<p>In the following sections, you will use your binding in Service Worker and ES modules format.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="reference-kv-from-durable-objects-and-workers">Reference KV from Durable Objects and Workers</h3>
@markup("md", "content/.markup/bodies/16173.md")
</aside>
<h3 id="bindings-in-service-worker-format">Bindings in Service Worker format</h3>
<p>In Service Worker syntax, your <code>TODO</code> KV namespace binding is defined in the global scope of your Worker. Your <code>TODO</code> KV namespace binding is available to use anywhere in your Worker application's code.</p>
<pre tabindex="0"><code class="language-js">addEventListener(&quot;fetch&quot;, async (event) =&gt; {&#10;  return await getTodos()&#10;});&#10;&#10;async function getTodos() {&#10;  // Get the value for the &quot;to-do:123&quot; key&#10;  // NOTE: Relies on the TODO KV binding that maps to the &quot;My Tasks&quot; namespace.&#10;  let value = await TODO.get(&quot;to-do:123&quot;);&#10;&#10;  // Return the value, as is, for the Response&#10;  event.respondWith(new Response(value));&#10;}&#10;</code></pre>
<h3 id="bindings-in-es-modules-format">Bindings in ES modules format</h3>
<p>In ES modules format, bindings are only available inside the <code>env</code> parameter that is provided at the entry point to your Worker.</p>
<p>To access the <code>TODO</code> KV namespace binding in your Worker code, the <code>env</code> parameter must be passed from the <code>fetch</code> handler in your Worker to the <code>getTodos</code> function.</p>
<pre tabindex="0"><code class="language-js">import { getTodos } from &#x27;./todos&#x27;&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    // Passing the env parameter so other functions&#10;    // can reference the bindings available in the Workers application&#10;    return await getTodos(env)&#10;  },&#10;};&#10;</code></pre>
<p>The following code represents a <code>getTodos</code> function that calls the <code>get</code> function on the <code>TODO</code> KV binding.</p>
<pre tabindex="0"><code class="language-js">async function getTodos(env) {&#10;  // NOTE: Relies on the TODO KV binding which has been provided inside of&#10;  // the env parameter of the `getTodos` function&#10;  let value = await env.TODO.get(&quot;to-do:123&quot;);&#10;  return new Response(value);&#10;}&#10;&#10;export { getTodos }&#10;</code></pre>
<h2 id="environment-variables">Environment variables</h2>
<p><a href="/workers/configuration/environment-variables/">Environment variables</a> are accessed differently in code written in ES modules format versus Service Worker format.</p>
<p>Review the following example environment variable configuration in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16176.md")
</div>
<h3 id="environment-variables-in-service-worker-format">Environment variables in Service Worker format</h3>
<p>In Service Worker format, the <code>API_ACCOUNT_ID</code> is defined in the global scope of your Worker application. Your <code>API_ACCOUNT_ID</code> environment variable is available to use anywhere in your Worker application's code.</p>
<pre tabindex="0"><code class="language-js">addEventListener(&quot;fetch&quot;, async (event) =&gt; {&#10;  console.log(API_ACCOUNT_ID) // Logs &quot;&lt;EXAMPLE-ACCOUNT-ID&gt;&quot;&#10;  return new Response(&quot;Hello, world!&quot;)&#10;})&#10;</code></pre>
<h3 id="environment-variables-in-es-modules-format">Environment variables in ES modules format</h3>
<p>In ES modules format, environment variables are available through the <code>env</code> parameter provided at the entrypoint to your Worker application:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    console.log(env.API_ACCOUNT_ID) // Logs &quot;&lt;EXAMPLE-ACCOUNT-ID&gt;&quot;&#10;    return new Response(&quot;Hello, world!&quot;)&#10;  },&#10;};&#10;</code></pre>
<p>You can also import <code>env</code> from <code>cloudflare:workers</code> to access environment variables from anywhere in your code, including the top-level scope:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16177.md")
</div>
<p>This approach is useful for initializing configuration or accessing environment variables from deeply nested functions without passing <code>env</code> through every function call. For more details, refer to <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">Importing <code>env</code> as a global</a>.</p>
<h2 id="cron-triggers">Cron Triggers</h2>
<p>To handle a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> event in a Worker written with ES modules syntax, implement a <a href="/workers/runtime-apis/handlers/scheduled/#syntax"><code>scheduled()</code> event handler</a>, which is the equivalent of listening for a <code>scheduled</code> event in Service Worker syntax.</p>
<p>This example code:</p>
<pre tabindex="0"><code class="language-js">addEventListener(&quot;scheduled&quot;, (event) =&gt; {&#10;  // ...&#10;});&#10;</code></pre>
<p>Then becomes:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async scheduled(event, env, ctx) {&#10;    // ...&#10;  },&#10;};&#10;</code></pre>
<h2 id="access-event-or-context-data">Access <code>event</code> or <code>context</code> data</h2>
<p>Workers often need access to data not in the <code>request</code> object. For example, sometimes Workers use <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> to delay execution. Workers using ES modules format can access <code>waitUntil</code> via the <code>context</code> parameter. Refer to <a href="/workers/runtime-apis/handlers/fetch/#parameters">ES modules parameters</a> for  more information.</p>
<p>This example code:</p>
<pre tabindex="0"><code class="language-js">async function triggerEvent(event) {&#10;  // Fetch some data&#10;  console.log(&#x27;cron processed&#x27;, event.scheduledTime);&#10;}&#10;&#10;// Initialize Worker&#10;addEventListener(&#x27;scheduled&#x27;, event =&gt; {&#10;  event.waitUntil(triggerEvent(event));&#10;});&#10;</code></pre>
<p>Then becomes:</p>
<pre tabindex="0"><code class="language-js">async function triggerEvent(event) {&#10;  // Fetch some data&#10;  console.log(&#x27;cron processed&#x27;, event.scheduledTime);&#10;}&#10;&#10;export default {&#10;  async scheduled(event, env, ctx) {&#10;    ctx.waitUntil(triggerEvent(event));&#10;  },&#10;};&#10;</code></pre>
<h2 id="service-worker-syntax">Service Worker syntax</h2>
<p>A Worker written in Service Worker syntax consists of two parts:</p>
<ol>
<li>An event listener that listens for <code>FetchEvents</code>.</li>
<li>An event handler that returns a <a href="/workers/runtime-apis/response/">Response</a> object which is passed to the event’s <code>.respondWith()</code> method.</li>
</ol>
<p>When a request is received on one of Cloudflare’s global network servers for a URL matching a Worker, Cloudflare's server passes the request to the Workers runtime. This dispatches a <code>FetchEvent</code> in the <a href="/workers/reference/how-workers-works/#isolates">isolate</a> where the Worker is running.</p>
<pre tabindex="0"><code class="language-js">addEventListener(&#x27;fetch&#x27;, event =&gt; {&#10;  event.respondWith(handleRequest(event.request));&#10;});&#10;&#10;async function handleRequest(request) {&#10;  return new Response(&#x27;Hello worker!&#x27;, {&#10;    headers: { &#x27;content-type&#x27;: &#x27;text/plain&#x27; },&#10;  });&#10;}&#10;</code></pre>
<p>Below is an example of the request response workflow:</p>
<ol>
<li>
<p>An event listener for the <code>FetchEvent</code> tells the script to listen for any request coming to your Worker. The event handler is passed the <code>event</code> object, which includes <code>event.request</code>, a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object which is a representation of the HTTP request that triggered the <code>FetchEvent</code>.</p>
</li>
<li>
<p>The call to <code>.respondWith()</code> lets the Workers runtime intercept the request in order to send back a custom response (in this example, the plain text <code>'Hello worker!'</code>).</p>
<ul>
<li>
<p>The <code>FetchEvent</code> handler typically culminates in a call to the method <code>.respondWith()</code> with either a <a href="/workers/runtime-apis/response/"><code>Response</code></a> or <code>Promise&lt;Response&gt;</code> that determines the response.</p>
</li>
<li>
<p>The <code>FetchEvent</code> object also provides <a href="/workers/runtime-apis/handlers/fetch/">two other methods</a> to handle unexpected exceptions and operations that may complete after a response is returned.</p>
</li>
</ul>
</li>
</ol>
<p>Learn more about <a href="/workers/runtime-apis/rpc/lifecycle/">the lifecycle methods of the <code>fetch()</code> handler</a>.</p>
<h3 id="supported-fetchevent-properties">Supported <code>FetchEvent</code> properties</h3>
<ul>
<li>
<p><code>event.type</code> string</p>
<ul>
<li>The type of event. This will always return <code>&quot;fetch&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>event.request</code> Request</p>
<ul>
<li>The incoming HTTP request.</li>
</ul>
</li>
<li>
<p><code>event.respondWith(responseResponse|<span style="margin-left:-6px">Promise</span>)</code> : void</p>
<ul>
<li>Refer to <a href="#respondwith"><code>respondWith</code></a>.</li>
</ul>
</li>
<li>
<p><code>event.waitUntil(promisePromise)</code> : void</p>
<ul>
<li>Refer to <a href="#waituntil"><code>waitUntil</code></a>.</li>
</ul>
</li>
<li>
<p><code>event.passThroughOnException()</code> : void</p>
<ul>
<li>Refer to <a href="#passthroughonexception"><code>passThroughOnException</code></a>.</li>
</ul>
</li>
</ul>
<h3 id="respondwith"><code>respondWith</code></h3>
<p>Intercepts the request and allows the Worker to send a custom response.</p>
<p>If a <code>fetch</code> event handler does not call <code>respondWith</code>, the runtime delivers the event to the next registered <code>fetch</code> event handler. In other words, while not recommended, this means it is possible to add multiple <code>fetch</code> event handlers within a Worker.</p>
<p>If no <code>fetch</code> event handler calls <code>respondWith</code>, then the runtime forwards the request to the origin as if the Worker did not. However, if there is no origin – or the Worker itself is your origin server, which is always true for <code>*.workers.dev</code> domains – then you must call <code>respondWith</code> for a valid response.</p>
<pre tabindex="0"><code class="language-js">// Format: Service Worker&#10;addEventListener(&#x27;fetch&#x27;, event =&gt; {&#10;  let { pathname } = new URL(event.request.url);&#10;&#10;  // Allow &quot;/ignore/*&quot; URLs to hit origin&#10;  if (pathname.startsWith(&#x27;/ignore/&#x27;)) return;&#10;&#10;  // Otherwise, respond with something&#10;  event.respondWith(handler(event));&#10;});&#10;</code></pre>
<h3 id="waituntil"><code>waitUntil</code></h3>
<p>The <code>waitUntil</code> command extends the lifetime of the <code>&quot;fetch&quot;</code> event. It accepts a <code>Promise</code>-based task which the Workers runtime will execute before the handler terminates but without blocking the response. For example, this is ideal for <a href="/workers/runtime-apis/cache/#put">caching responses</a> or handling logging.</p>
<p>With the Service Worker format, <code>waitUntil</code> is available within the <code>event</code> because it is a native <code>FetchEvent</code> property.</p>
<p>With the ES modules format, <code>waitUntil</code> is moved and available on the <code>context</code> parameter object.</p>
<pre tabindex="0"><code class="language-js">// Format: Service Worker&#10;addEventListener(&#x27;fetch&#x27;, event =&gt; {&#10;  event.respondWith(handler(event));&#10;});&#10;&#10;async function handler(event) {&#10;  // Forward / Proxy original request&#10;  let res = await fetch(event.request);&#10;&#10;  // Add custom header(s)&#10;  res = new Response(res.body, res);&#10;  res.headers.set(&#x27;x-foo&#x27;, &#x27;bar&#x27;);&#10;&#10;  // Cache the response&#10;  // NOTE: Does NOT block / wait&#10;  event.waitUntil(caches.default.put(event.request, res.clone()));&#10;&#10;  // Done&#10;  return res;&#10;}&#10;</code></pre>
<h3 id="passthroughonexception"><code>passThroughOnException</code></h3>
<p>The <code>passThroughOnException</code> method prevents a runtime error response when the Worker throws an unhandled exception. Instead, the script will <a href="https://community.microfocus.com/cyberres/b/sws-22/posts/security-fundamentals-part-1-fail-open-vs-fail-closed">fail open</a>, which will proxy the request to the origin server as though the Worker was never invoked.</p>
<p>To prevent JavaScript errors from causing entire requests to fail on uncaught exceptions, <code>passThroughOnException()</code> causes the Workers runtime to yield control to the origin server.</p>
<p>With the Service Worker format, <code>passThroughOnException</code> is added to the <code>FetchEvent</code> interface, making it available within the <code>event</code>.</p>
<p>With the ES modules format, <code>passThroughOnException</code> is available on the <code>context</code> parameter object.</p>
<pre tabindex="0"><code class="language-js">// Format: Service Worker&#10;addEventListener(&#x27;fetch&#x27;, event =&gt; {&#10;  // Proxy to origin on unhandled/uncaught exceptions&#10;  event.passThroughOnException();&#10;  throw new Error(&#x27;Oops&#x27;);&#10;});&#10;</code></pre>
