---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/
  description: Understand the architecture of Workers for Platforms, including dispatch namespaces, dynamic dispatch Workers, user Workers, and outbound Workers.
  full_title: How Workers for Platforms works · Cloudflare for Platforms docs
  head_html: <title>How Workers for Platforms works · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the architecture of Workers for Platforms, including dispatch namespaces, dynamic dispatch Workers, user Workers, and outbound Workers."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/index.md"><meta property="og:title" content="How Workers for Platforms works · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the architecture of Workers for Platforms, including dispatch namespaces, dynamic dispatch Workers, user Workers, and outbound Workers."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#page","headline":"How Workers for Platforms works \u00b7 Cloudflare for Platforms docs","description":"Understand the architecture of Workers for Platforms, including dispatch namespaces, dynamic dispatch Workers, user Workers, and outbound Workers.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/
  schema: 1
---
<h2 id="architecture">Architecture</h2>
<p>If you are familiar with <a href="/workers/">Workers</a>, Workers for Platforms introduces four key components: dispatch namespaces, dynamic dispatch Workers, user Workers, and optionally outbound Workers.</p>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-1.svg" alt="Workers for Platforms architecture" /></p>
<h3 id="dispatch-namespace">Dispatch namespace</h3>
<p>A dispatch namespace is a container that holds all of your customers' Workers. Your platform takes the code your customers write, and then makes an API request to deploy that code as a user Worker to a namespace — for example <code>staging</code> or <code>production</code>. Compared to <a href="/workers/">Workers</a>, this provides:</p>
<ul>
<li><strong>Unlimited number of Workers</strong> - No per-account script limits apply to Workers in a namespace</li>
<li><strong>Isolation by default</strong> - Each user Worker in a namespace runs in <a href="/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/">untrusted mode</a> — user Workers never share a cache even when running on the same Cloudflare zone, and cannot access the <code>request.cf</code> object</li>
<li><strong>Dynamic invocation</strong> - Your dynamic dispatch Worker can call any Worker in the namespace using <code>env.DISPATCHER.get(&quot;worker-name&quot;)</code></li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/4060.md")
</aside>
<h3 id="dynamic-dispatch-worker">Dynamic dispatch Worker</h3>
<p>A dynamic dispatch Worker is the entry point for all requests to your platform. Your dynamic dispatch Worker:</p>
<ul>
<li><strong>Routes requests</strong> - Determines which customer Worker should handle each request based on hostname, path, headers, or any other criteria</li>
<li><strong>Runs platform logic</strong> - Executes authentication, rate limiting, or request validation before customer code runs</li>
<li><strong>Sets per-customer limits</strong> - Enforces <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/">custom limits</a> on CPU time and subrequests based on plan type</li>
<li><strong>Sanitizes responses</strong> - Modifies or filters responses from customer Workers</li>
</ul>
<p>The dynamic dispatch Worker uses a <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">dispatch namespace binding</a> to invoke user Workers:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		// Determine which customer Worker to call&#10;		const customerName = new URL(request.url).hostname.split(&quot;.&quot;)[0];&#10;&#10;		// Get and invoke the customer&#x27;s Worker&#10;		const userWorker = env.DISPATCHER.get(customerName);&#10;		return userWorker.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h3 id="user-workers">User Workers</h3>
<p>User Workers contain code written by your customers. Your customer sends their code to your platform, and then you make an API request to deploy a user Worker on their behalf. User Workers are deployed to a dispatch namespace and invoked by your dynamic dispatch Worker. You can provide user Workers with <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">bindings</a> to access KV, D1, R2, and other Cloudflare resources.</p>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-6.svg" alt="Deployment and management flow" /></p>
<h3 id="outbound-worker-optional">Outbound Worker (optional)</h3>
<p>An <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">outbound Worker</a> intercepts <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a> requests made by user Workers. Use it to:</p>
<ul>
<li><strong>Control egress</strong> - Block or allow external API calls from customer code</li>
<li><strong>Log requests</strong> - Track what external services customers are calling</li>
<li><strong>Modify requests</strong> - Add authentication headers or transform requests before they leave your platform</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/programmable-platforms/programmable-platforms-3.svg" alt="Outbound Worker egress control pattern" /></p>
<h3 id="request-lifecycle">Request lifecycle</h3>
<ol>
<li>A request arrives at your dynamic dispatch Worker (for example, <code>customer-a.example.com/api</code>)</li>
<li>Your dynamic dispatch Worker determines which user Worker should handle the request</li>
<li>The dynamic dispatch Worker calls <code>env.DISPATCHER.get(&quot;customer-a&quot;)</code> to get the user Worker</li>
<li>The user Worker executes. If it makes external <code>fetch()</code> calls and an outbound Worker is configured, those requests pass through the outbound Worker first.</li>
<li>The user Worker returns a response</li>
<li>Your dynamic dispatch Worker can optionally modify the response before returning it</li>
</ol>
<hr />
<h2 id="workers-for-platforms-versus-service-bindings">Workers for Platforms versus Service bindings</h2>
<p>Both Workers for Platforms and <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> enable Worker-to-Worker communication. Use Service bindings when you know exactly which Workers need to communicate. Use Workers for Platforms when user Workers are uploaded dynamically by your customers.</p>
<p>You can use both simultaneously - your dynamic dispatch Worker can use Service bindings to call internal services while also dispatching to user Workers in a namespace.</p>
