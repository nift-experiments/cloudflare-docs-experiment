---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/
  description: Understand how a Durable Object is created, activated, handles requests, and is eventually evicted.
  full_title: Lifecycle of a Durable Object · Cloudflare Durable Objects docs
  head_html: <title>Lifecycle of a Durable Object · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how a Durable Object is created, activated, handles requests, and is eventually evicted."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/index.md"><meta property="og:title" content="Lifecycle of a Durable Object · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how a Durable Object is created, activated, handles requests, and is eventually evicted."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/#page","headline":"Lifecycle of a Durable Object \u00b7 Cloudflare Durable Objects docs","description":"Understand how a Durable Object is created, activated, handles requests, and is eventually evicted.","url":"https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/concepts/durable-object-lifecycle/
  schema: 1
---
<p>This section describes the lifecycle of a <a href="/durable-objects/concepts/what-are-durable-objects/">Durable Object</a>.</p>
<p>To use a Durable Object you need to create a <a href="/durable-objects/api/stub/">Durable Object Stub</a>.
Simply creating the Durable Object Stub does not send a request to the Durable Object, and therefore the Durable Object is not yet instantiated.
A request is sent to the Durable Object and its lifecycle begins only once a method is invoked on the Durable Object Stub.</p>
<pre tabindex="0"><code class="language-js">const stub = env.MY_DURABLE_OBJECT.getByName(&quot;foo&quot;);&#10;// Now the request is sent to the remote Durable Object.&#10;const rpcResponse = await stub.sayHello();&#10;</code></pre>
<h2 id="durable-object-lifecycle-state-transitions">Durable Object Lifecycle state transitions</h2>
<p>A Durable Object can be in one of the following states at any moment:</p>
<table>
<thead>
<tr>
<th>State</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Active, in-memory</strong></td>
<td>The Durable Object runs, in memory, and handles incoming requests.</td>
</tr>
<tr>
<td><strong>Idle, in-memory non-hibernateable</strong></td>
<td>The Durable Object waits for the next incoming request/event, but does not satisfy the criteria for hibernation.</td>
</tr>
<tr>
<td><strong>Idle, in-memory hibernateable</strong></td>
<td>The Durable Object waits for the next incoming request/event and satisfies the criteria for hibernation. It is up to the runtime to decide when to hibernate the Durable Object. Currently, it is after 10 seconds of inactivity while in this state.</td>
</tr>
<tr>
<td><strong>Hibernated</strong></td>
<td>The Durable Object is removed from memory. Hibernated WebSocket connections stay connected.</td>
</tr>
<tr>
<td><strong>Inactive</strong></td>
<td>The Durable Object is completely removed from the host process and might need to cold start. This is the initial state of all Durable Objects.</td>
</tr>
</tbody>
</table>
<p>This is how a Durable Object transitions among these states (each state is in a rounded rectangle).</p>
<p><img src="/assets/upstream/images/durable-objects/durable-object-lifecycle.png" alt="Lifecycle of a Durable Object" /></p>
<p>Assuming a Durable Object does not run, the first incoming request or event (like an alarm) will execute the <code>constructor()</code> of the Durable Object class, then run the corresponding function invoked.</p>
<p>At this point the Durable Object is in the <strong>active in-memory state</strong>.</p>
<p>Once all incoming requests or events have been processed, the Durable Object remains idle in-memory for a few seconds either in a hibernateable state or in a non-hibernateable state.</p>
<p>Hibernation can only occur if <strong>all</strong> of the conditions below are true:</p>
<ul>
<li>No <code>setTimeout</code>/<code>setInterval</code> scheduled callbacks are set, since there would be no way to recreate the callback after hibernating.</li>
<li>No in-progress awaited <code>fetch()</code> exists, since it is considered to be waiting for I/O.</li>
<li>No WebSocket standard API is used.</li>
<li>No request/event is still being processed, because hibernating would mean losing track of the async function which is eventually supposed to return a response to that request.</li>
<li>No active outbound TCP socket (<code>connect()</code>) or outbound WebSocket connection exists.</li>
</ul>
<p>After 10 seconds of no incoming request or event, and all the above conditions satisfied, the Durable Object will transition into the <strong>hibernated</strong> state.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8236.md")
</aside>
<p>If any of the above conditions is false, the Durable Object remains in-memory, in the <strong>idle, in-memory, non-hibernateable</strong> state.</p>
<p>In case of an incoming request or event while in the <strong>hibernated</strong> state, the <code>constructor()</code> will run again, and the Durable Object will transition to the <strong>active, in-memory</strong> state and execute the invoked function.</p>
<p>While in the <strong>idle, in-memory, non-hibernateable</strong> state, after 70-140 seconds of inactivity (no incoming requests or events), the Durable Object will be evicted entirely from memory and potentially from the Cloudflare host and transition to the <strong>inactive</strong> state.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="outbound-connections-keep-durable-objects-alive">Outbound connections keep Durable Objects alive</h3>
@markup("md", "content/.markup/bodies/8235.md")
</aside>
<p>Objects in the <strong>hibernated</strong> state keep their Websocket clients connected, and the runtime decides if and when to transition the object to the <strong>inactive</strong> state (for example deciding to move the object to a different host) thus restarting the lifecycle.</p>
<p>The next incoming request or event starts the cycle again.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="lifecycle-states-incurring-duration-charges">Lifecycle states incurring duration charges</h3>
@markup("md", "content/.markup/bodies/8234.md")
</aside>
<h2 id="shutdown-behavior">Shutdown behavior</h2>
<p>Durable Objects will occasionally shut down and objects are restarted, which will run your Durable Object class constructor. This can happen for various reasons, including:</p>
<ul>
<li>New Worker <a href="/workers/versions-and-deployments/">deployments</a> with code updates</li>
<li>Lack of requests to an object following the state transitions documented above</li>
<li>Cloudflare updates to the Workers runtime system</li>
<li>Workers runtime decisions on where to host objects</li>
</ul>
<p>When a Durable Object is shut down, the object instance is automatically restarted and new requests are routed to the new instance. In-flight requests are handled as follows:</p>
<ul>
<li><strong>HTTP &amp; RPC requests</strong>: In-flight requests are allowed to finish if they do not access a Durable Object's storage.  If a request attempts to access a Durable Object's storage, it will be stopped immediately and return an error to maintain Durable Objects global uniqueness property. When the Worker runtime system is being updated, in-flight requests have up to 30 seconds to complete.</li>
<li><strong>WebSocket connections</strong>: WebSocket requests are terminated automatically during shutdown. This is so that the new instance can take over the connection as soon as possible.</li>
<li><strong>Other invocations (email, cron)</strong>: Other invocations are treated similarly to HTTP requests.</li>
</ul>
<p>It is important to ensure that any services using Durable Objects are designed to handle the possibility of a Durable Object being shut down.</p>
<h3 id="code-updates">Code updates</h3>
<p>When your Durable Object code is updated, your Worker and Durable Objects are released globally in an eventually consistent manner. This will cause a Durable Object to shut down, with the behavior described above. Updates can also create a situation where a request reaches a new version of your Worker in one location, and calls to a Durable Object still running a previous version elsewhere. Refer to <a href="/durable-objects/platform/known-issues/#code-updates">Code updates</a> for more information about handling this scenario.</p>
<h3 id="working-without-shutdown-hooks">Working without shutdown hooks</h3>
<p>Durable Objects may shut down at any time due to deployments, inactivity, or runtime decisions. Rather than relying on shutdown hooks (which are not provided), design your application to write state incrementally.</p>
<p>Shutdown hooks or lifecycle callbacks that run before shutdown are not provided because Cloudflare cannot guarantee these hooks would execute in all cases, and external software may rely too heavily on these (unreliable) hooks.</p>
<p>Instead of relying on shutdown hooks, you can regularly write to storage to recover gracefully from shutdowns.</p>
<p>For example, if you are processing a stream of data and need to save your progress, write your position to storage as you go rather than waiting to persist it at the end:</p>
<pre tabindex="0"><code class="language-js">// Good: Write progress as you go&#10;async processData(data) {&#10;  data.forEach(async (item, index) =&gt; {&#10;    await this.processItem(item);&#10;    // Save progress frequently&#10;    await this.ctx.storage.put(&quot;lastProcessedIndex&quot;, index);&#10;  });&#10;}&#10;</code></pre>
<p>While this may feel unintuitive, Durable Object storage writes are fast and synchronous, so you can persist state with minimal performance concerns.</p>
<p>This approach ensures your Durable Object can safely resume from any point, even if it shuts down unexpectedly.</p>
