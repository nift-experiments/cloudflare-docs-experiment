---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/
  description: Create a dynamic dispatch Worker to route incoming requests to user Workers in your dispatch namespace.
  full_title: Dynamic dispatch Worker · Cloudflare for Platforms docs
  head_html: <title>Dynamic dispatch Worker · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a dynamic dispatch Worker to route incoming requests to user Workers in your dispatch namespace."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/index.md"><meta property="og:title" content="Dynamic dispatch Worker · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a dynamic dispatch Worker to route incoming requests to user Workers in your dispatch namespace."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/#page","headline":"Dynamic dispatch Worker \u00b7 Cloudflare for Platforms docs","description":"Create a dynamic dispatch Worker to route incoming requests to user Workers in your dispatch namespace.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/
  schema: 1
---
<p>A <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dynamic dispatch Worker</a> is a specialized routing Worker that directs incoming requests to the appropriate user Workers in your dispatch namespace. Instead of using <a href="/workers/configuration/routing/routes/">Workers Routes</a>, dispatch Workers let you programmatically control request routing through code.</p>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-1.svg" alt="Figure 1: Workers for Platforms: Main Flow" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4223.md")
</aside>
<h4 id="why-use-a-dynamic-dispatch-worker">Why use a dynamic dispatch Worker?</h4>
<ul>
<li><strong>Scale</strong>: Route requests to millions of hostnames to different Workers, without defining <a href="/workers/configuration/routing/routes/">Workers Routes</a> configuration for each one</li>
<li><strong>Custom routing logic</strong>: Write code to determine exactly how requests should be routed. For example:
<ul>
<li>Store hostname-to-Worker mappings in <a href="/kv/">Workers KV</a> and look them up dynamically</li>
<li>Route requests based on subdomain, path, headers, or other request properties</li>
<li>Use <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a> attached to <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a> for routing decisions</li>
</ul>
</li>
<li><strong>Add platform functionality</strong>: Build additional features at the routing layer:
<ul>
<li>Run authentication checks before requests reach user Workers</li>
<li>Remove or add headers or metadata from incoming requests</li>
<li>Attach useful context like user IDs or account information</li>
<li>Transform requests or responses as needed</li>
</ul>
</li>
</ul>
<h3 id="configure-the-dispatch-namespace-binding">Configure the dispatch namespace binding</h3>
<p>To allow your dynamic dispatch Worker to dynamically route requests to Workers in a namespace, you need to configure a dispatch namespace <a href="/workers/runtime-apis/bindings/">binding</a>. This binding enables your dynamic dispatch Worker to call any user Worker within that namespace using <code>env.dispatcher.get()</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4224.md")
</div>
<p>Once the binding is configured, your dynamic dispatch Worker can route requests to any Worker in the namespace. Below are common routing patterns you can implement in your dispatcher.</p>
<h3 id="pass-data-and-capabilities-per-request">Pass data and capabilities per request</h3>
<p>When your dispatch Worker invokes a user Worker, it can send additional values with that invocation. For example, the dispatch Worker can authenticate a request and send the resulting user ID, permissions, or account information to the user Worker.</p>
<p>This is useful when the context should come from your platform code instead of directly from the incoming request. To send this context, add the values to <a href="/workers/runtime-apis/context/#props"><code>props</code></a> in the second argument to <code>env.DISPATCHER.get()</code>.</p>
<p>In the dispatch Worker, pass the user ID and permissions when you retrieve the user Worker from the dispatch namespace:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4225.md")
</div>
<p>In the user Worker, receive these values through <code>ctx.props</code>. In a <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#the-workerentrypoint-class"><code>WorkerEntrypoint</code></a>, access them through <code>this.ctx.props</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4226.md")
</div>
<p>These data values are visible to the user code. The dispatch Worker can select different props for each invocation without changing or redeploying the user Worker.</p>
<h4 id="give-access-to-specific-platform-functions">Give access to specific platform functions</h4>
<p>You may not want the user Worker to have direct access to all the context from the dispatch Worker. For example, authentication data is managed by your platform and should remain hidden from user code.</p>
<p>In this case, pass a <strong>capability</strong> instead of passing the data directly. A capability exposes specific methods that the user Worker can call, while the underlying data, credentials, and resources remain in the dispatch Worker. Workers passes the capability as an <a href="/workers/runtime-apis/rpc/#structured-cloneable-types-and-more">RPC stub</a>, which forwards method calls to your dispatch Worker.</p>
<p>To create a capability, export a <code>WorkerEntrypoint</code> class from your dispatch Worker. The <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code></a> object lets the dispatch Worker create an RPC stub for that exported class, which it can then pass to the user Worker.</p>
<p>The following example shows this pattern. The dispatch Worker uses a site ID and visitor ID to create a <code>Connector</code> capability. It passes the capability to the user Worker through <code>props</code>, without passing those IDs as separate data values. The user Worker can then call the methods exposed by <code>Connector</code>.</p>
<p>In the dispatch Worker, define the <code>Connector</code> methods, configure the connector with the site and visitor IDs, and pass it to the user Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4227.md")
</div>
<p>In the user Worker, receive the capability through <code>this.ctx.props</code> and call its exposed methods:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4228.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4222.md")
</aside>
<h4 id="pass-data-to-an-outbound-worker">Pass data to an Outbound Worker</h4>
<p>To send data from the dispatch Worker to an <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">Outbound Worker</a>, first declare the parameter name in the dispatch namespace binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4229.md")
</div>
<p>In the dispatch Worker, pass a value with the same name through the <code>outbound</code> option in the third argument to <code>env.DISPATCHER.get()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4230.md")
</div>
<p>In the Outbound Worker, access the value as an environment binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4231.md")
</div>
<p>Outbound Worker parameters support JSON values. They are separate from the <code>props</code> in the second argument, which are passed to the user Worker.</p>
<h3 id="routing-examples">Routing examples</h3>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-2.svg" alt="Figure 2: Workers for Platforms: Main Flow" /></p>
<h4 id="kv-based-routing">KV-Based Routing</h4>
<p>Store the routing mappings in <a href="/kv/">Workers KV</a>. This allows you to modify your routing logic without requiring you to change or redeploy the dynamic dispatch Worker.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		try {&#10;			const url = new URL(request.url);&#10;&#10;			// Use hostname, path, or any combination as the routing key&#10;			const routingKey = url.hostname;&#10;&#10;			// Lookup user Worker name from KV store&#10;			const userWorkerName = await env.USER_ROUTING.get(routingKey);&#10;&#10;			if (!userWorkerName) {&#10;				return new Response(&quot;Route not configured&quot;, { status: 404 });&#10;			}&#10;&#10;			// Optional: Cache the KV lookup result&#10;			const userWorker = env.DISPATCHER.get(userWorkerName);&#10;			return await userWorker.fetch(request);&#10;		} catch (e) {&#10;			if (e.message.startsWith(&quot;Worker not found&quot;)) {&#10;				return new Response(&quot;&quot;, { status: 404 });&#10;			}&#10;			return new Response(e.message, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h4 id="subdomain-based-routing">Subdomain-Based Routing</h4>
<p>Route subdomains to the corresponding Worker. For example, <code>my-customer.example.com</code> will route to the Worker named <code>my-customer</code> in the dispatch namespace.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		try {&#10;			// Extract user Worker name from subdomain&#10;			// Example: customer1.example.com -&gt; customer1&#10;			const url = new URL(request.url);&#10;			const userWorkerName = url.hostname.split(&quot;.&quot;)[0];&#10;&#10;			// Get user Worker from dispatch namespace&#10;			const userWorker = env.DISPATCHER.get(userWorkerName);&#10;			return await userWorker.fetch(request);&#10;		} catch (e) {&#10;			if (e.message.startsWith(&quot;Worker not found&quot;)) {&#10;				// User Worker doesn&#x27;t exist in dispatch namespace&#10;				return new Response(&quot;&quot;, { status: 404 });&#10;			}&#10;			// Could be any other exception from fetch() or from the dispatched Worker&#10;			return new Response(e.message, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h4 id="path-based-routing">Path-Based routing</h4>
<p>Route URL paths to the corresponding Worker. For example, <code>example.com/customer-1</code> will route to the Worker named <code>customer-1</code> in the dispatch namespace.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		try {&#10;			const url = new URL(request.url);&#10;			const pathParts = url.pathname.split(&quot;/&quot;).filter(Boolean);&#10;&#10;			if (pathParts.length === 0) {&#10;				return new Response(&quot;Invalid path&quot;, { status: 400 });&#10;			}&#10;&#10;			// example.com/customer-1 -&gt; routes to &#x27;customer-1&#x27; worker&#10;			const userWorkerName = pathParts[0];&#10;&#10;			const userWorker = env.DISPATCHER.get(userWorkerName);&#10;			return await userWorker.fetch(request);&#10;		} catch (e) {&#10;			if (e.message.startsWith(&quot;Worker not found&quot;)) {&#10;				return new Response(&quot;&quot;, { status: 404 });&#10;			}&#10;			return new Response(e.message, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
