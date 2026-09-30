---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/
  description: Facilitate Worker-to-Worker communication.
  full_title: Service bindings - Runtime APIs · Cloudflare Workers docs
  head_html: <title>Service bindings - Runtime APIs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Facilitate Worker-to-Worker communication."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/index.md"><meta property="og:title" content="Service bindings - Runtime APIs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Facilitate Worker-to-Worker communication."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Bindings"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/#page","headline":"Service bindings - Runtime APIs \u00b7 Cloudflare Workers docs","description":"Facilitate Worker-to-Worker communication.","url":"https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Bindings"]}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/bindings/service-bindings/
  schema: 1
---
<h2 id="about-service-bindings">About Service bindings</h2>
<p>Service bindings allow one Worker to call into another, without going through a publicly-accessible URL. A Service binding allows Worker A to call a method on Worker B, or to forward a request from Worker A to Worker B.</p>
<p>Service bindings provide the separation of concerns that microservice or service-oriented architectures provide, without configuration pain, performance overhead or need to learn RPC protocols.</p>
<ul>
<li><strong>Service bindings are fast.</strong> When you use Service Bindings, there is zero overhead or added latency. By default, both Workers run on the same thread of the same Cloudflare server. And when you enable <a href="/workers/configuration/placement/">Smart Placement</a>, each Worker runs in the optimal location for overall performance.</li>
<li><strong>Service bindings are not just HTTP.</strong> Worker A can expose methods that can be directly called by Worker B. Communicating between services only requires writing JavaScript methods and classes.</li>
<li><strong>Service bindings don't increase costs.</strong> You can split apart functionality into multiple Workers, without incurring additional costs. Learn more about <a href="/workers/platform/pricing/#service-bindings">pricing for Service Bindings</a>.</li>
</ul>
<p><img src="/assets/upstream/images/workers/platform/bindings/service-bindings-comparison.png" alt="Service bindings are a zero-cost abstraction" /></p>
<p>Service bindings are commonly used to:</p>
<ul>
<li><strong>Provide a shared internal service to multiple Workers.</strong> For example, you can deploy an authentication service as its own Worker, and then have any number of separate Workers communicate with it via Service bindings.</li>
<li><strong>Isolate services from the public Internet.</strong> You can deploy a Worker that is not reachable via the public Internet, and can only be reached via an explicit Service binding that another Worker declares.</li>
<li><strong>Allow teams to deploy code independently.</strong> Team A can deploy their Worker on their own release schedule, and Team B can deploy their Worker separately.</li>
</ul>
<h2 id="configuration">Configuration</h2>
<p>You add a Service binding by modifying the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> of the caller — the Worker that you want to be able to initiate requests.</p>
<p>For example, if you want Worker A to be able to call Worker B — you'd add the following to the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for Worker A:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17263.md")
</div>
<ul>
<li><code>binding</code>: The name of the key you want to expose on the <code>env</code> object.</li>
<li><code>service</code>: The name of the target Worker you would like to communicate with. This Worker must be on your Cloudflare account.</li>
</ul>
<h2 id="interfaces">Interfaces</h2>
<p>Worker A that declares a Service binding to Worker B can call Worker B in two different ways:</p>
<ol>
<li><a href="/workers/runtime-apis/bindings/service-bindings/rpc">RPC</a> lets you communicate between Workers using function calls that you define. For example, <code>await env.BINDING_NAME.myMethod(arg1)</code>. This is recommended for most use cases, and allows you to create your own internal APIs that your Worker makes available to other Workers.</li>
<li><a href="/workers/runtime-apis/bindings/service-bindings/http">HTTP</a> lets you communicate between Workers by calling the <a href="/workers/runtime-apis/handlers/fetch"><code>fetch()</code> handler</a> from other Workers, sending <code>Request</code> objects and receiving <code>Response</code> objects back. For example, <code>env.BINDING_NAME.fetch(request)</code>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-access-context">Cloudflare Access context</h3>
@markup("md", "content/.markup/bodies/17262.md")
</aside>
<h2 id="example-build-your-first-service-binding-using-rpc">Example — build your first Service binding using RPC</h2>
<p>This example <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#the-workerentrypoint-class">extends the <code>WorkerEntrypoint</code> class</a> to support RPC-based Service bindings.
First, create the Worker that you want to communicate with. Let's call this &quot;Worker B&quot;. Worker B exposes the public method, <code>add(a, b)</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17264.md")
</div>
<pre tabindex="0"><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export default class WorkerB extends WorkerEntrypoint {&#10;	// Currently, entrypoints without a named handler are not supported&#10;	async fetch() {&#10;		return new Response(null, { status: 404 });&#10;	}&#10;&#10;	async add(a, b) {&#10;		return a + b;&#10;	}&#10;}&#10;</code></pre>
<p>Next, create the Worker that will call Worker B. Let's call this &quot;Worker A&quot;. Worker A declares a binding to Worker B. This is what gives it permission to call public methods on Worker B.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17265.md")
</div>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const result = await env.WORKER_B.add(1, 2);&#10;		return new Response(result);&#10;	},&#10;};&#10;</code></pre>
<p>To run both Worker A and Worker B in local development, you must run two instances of <a href="/workers/wrangler">Wrangler</a> in your terminal. For each Worker, open a new terminal and run <a href="/workers/wrangler/commands#dev"><code>npx wrangler@latest dev</code></a>.</p>
<p>Each Worker is deployed separately.</p>
<h2 id="lifecycle">Lifecycle</h2>
<p>The Service bindings API is asynchronous — you must <code>await</code> any method you call. If Worker A invokes Worker B via a Service binding, and Worker A does not await the completion of Worker B, Worker B will be terminated early.</p>
<p>For more about the lifecycle of calling a Worker over a Service Binding via RPC, refer to the <a href="/workers/runtime-apis/rpc/lifecycle">RPC Lifecycle</a> docs.</p>
<h2 id="local-development">Local development</h2>
<p>Local development is supported for Service bindings. For each Worker, open a new terminal and use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> in the relevant directory. When running <code>wrangler dev</code>, service bindings will show as <code>connected</code>/<code>not connected</code> depending on whether Wrangler can find a running <code>wrangler dev</code> session for that Worker. For example:</p>
<pre tabindex="0"><code class="language-sh">$ wrangler dev&#10;...&#10;Your worker has access to the following bindings:&#10;&#45; Services:&#10;  &#45; SOME_OTHER_WORKER: some-other-worker [connected]&#10;  &#45; ANOTHER_WORKER: another-worker [not connected]&#10;</code></pre>
<p>Wrangler also supports running multiple Workers at once with one command. To try it out, pass multiple <code>-c</code> flags to Wrangler, like this: <code>wrangler dev -c wrangler.json -c ../other-worker/wrangler.json</code>. The first config will be treated as the <em>primary</em> worker, which will be exposed over HTTP as usual at <code>http://localhost:8787</code>. The remaining config files will be treated as <em>secondary</em> and will only be accessible via a service binding from the primary worker.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17261.md")
</aside>
<h2 id="deployment">Deployment</h2>
<p>Workers using Service bindings are deployed separately.</p>
<p>When getting started and deploying for the first time, this means that the target Worker (Worker B in the examples above) must be deployed first, before Worker A. Otherwise, when you attempt to deploy Worker A, deployment will fail, because Worker A declares a binding to Worker B, which does not yet exist.</p>
<p>When making changes to existing Workers, in most cases you should:</p>
<ul>
<li>Deploy changes to Worker B first, in a way that is compatible with the existing Worker A. For example, add a new method to Worker B.</li>
<li>Next, deploy changes to Worker A. For example, call the new method on Worker B, from Worker A.</li>
<li>Finally, remove any unused code. For example, delete the previously used method on Worker B.</li>
</ul>
<h2 id="smart-placement">Smart Placement</h2>
<p><a href="/workers/configuration/placement/">Smart Placement</a> automatically places your Worker in an optimal location that minimizes latency.</p>
<p>You can use Smart Placement together with Service bindings to split your Worker into two services:</p>
<p><img src="/assets/upstream/images/workers/platform/smart-placement-service-bindings.png" alt="Smart Placement and Service Bindings" /></p>
<p>Refer to the <a href="/workers/configuration/placement/#multiple-workers">docs on Smart Placement</a> for more.</p>
<h2 id="limits">Limits</h2>
<p>Service bindings have the following limits:</p>
<ul>
<li>Each request to a Worker via a Service binding counts toward your <a href="/workers/platform/limits/#subrequests">subrequest limit</a>.</li>
<li>A single request has a maximum of 32 Worker invocations, and each call to a Service binding counts towards this limit. Subsequent calls will throw an exception.</li>
<li>Calling a service binding does not count towards <a href="/workers/platform/limits/#simultaneous-open-connections">simultaneous open connection limits</a></li>
</ul>
