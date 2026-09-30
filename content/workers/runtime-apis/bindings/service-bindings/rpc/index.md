---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/
  description: Facilitate Worker-to-Worker communication via RPC.
  full_title: Service bindings - RPC (WorkerEntrypoint) · Cloudflare Workers docs
  head_html: <title>Service bindings - RPC (WorkerEntrypoint) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Facilitate Worker-to-Worker communication via RPC."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/index.md"><meta property="og:title" content="Service bindings - RPC (WorkerEntrypoint) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Facilitate Worker-to-Worker communication via RPC."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="RPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/#page","headline":"Service bindings - RPC (WorkerEntrypoint) \u00b7 Cloudflare Workers docs","description":"Facilitate Worker-to-Worker communication via RPC.","url":"https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["RPC"]}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/bindings/service-bindings/rpc/
  schema: 1
---
<p><a href="/workers/runtime-apis/bindings/service-bindings">Service bindings</a> allow one Worker to call into another, without going through a publicly-accessible URL.</p>
<p>You can use Service bindings to create your own internal APIs that your Worker makes available to other Workers. This can be done by extending the built-in <code>WorkerEntrypoint</code> class, and adding your own public methods. These public methods can then be directly called by other Workers on your Cloudflare account that declare a <a href="/workers/runtime-apis/bindings">binding</a> to this Worker.</p>
<p>The <a href="/workers/runtime-apis/rpc">RPC system in Workers</a> is designed feel as similar as possible to calling a JavaScript function in the same Worker. In most cases, you should be able to write code in the same way you would if everything was in a single Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17226.md")
</aside>
<h2 id="example">Example</h2>
<p>For example, the following Worker implements the public method <code>add(a, b)</code>:</p>
<p>For example, if Worker B implements the public method <code>add(a, b)</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17227.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17230.md")
</div></div>
<p>Worker A can declare a <a href="/workers/runtime-apis/bindings">binding</a> to Worker B:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17231.md")
</div>
<p>Making it possible for Worker A to call the <code>add()</code> method from Worker B:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17234.md")
</div></div>
<p>You do not need to learn, implement, or think about special protocols to use the RPC system. The client, in this case Worker A, calls Worker B and tells it to execute a specific procedure using specific arguments that the client provides. This is accomplished with standard JavaScript classes.</p>
<h2 id="the-workerentrypoint-class">The <code>WorkerEntrypoint</code> Class</h2>
<p>To provide RPC methods from your Worker, you must extend the <code>WorkerEntrypoint</code> class, as shown in the example below:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17237.md")
</div></div>
<p>A new instance of the class is created every time the Worker is called. Note that even though the Worker is implemented as a class, it is still stateless — the class instance only lasts for the duration of the invocation. If you need to persist or coordinate state in Workers, you should use <a href="/durable-objects">Durable Objects</a>.</p>
<h3 id="bindings-env">Bindings (<code>env</code>)</h3>
<p>The <a href="/workers/runtime-apis/bindings"><code>env</code></a> object is exposed as a class property of the <code>WorkerEntrypoint</code> class.</p>
<p>For example, a Worker that declares a binding to the <a href="/workers/configuration/environment-variables/">environment variable</a> <code>GREETING</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17238.md")
</div>
<p>Can access it by calling <code>this.env.GREETING</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17241.md")
</div></div>
<p>You can use any type of <a href="/workers/runtime-apis/bindings">binding</a> this way.</p>
<h3 id="lifecycle-methods-ctx">Lifecycle methods (<code>ctx</code>)</h3>
<p>The <a href="/workers/runtime-apis/context"><code>ctx</code></a> object is exposed as a class property of the <code>WorkerEntrypoint</code> class.</p>
<p>For example, you can extend the lifetime of the invocation context by calling the <code>waitUntil()</code> method:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17244.md")
</div></div>
<h3 id="fetching-static-assets">Fetching static assets</h3>
<p>If your Worker has a <a href="/workers/static-assets/binding/">static assets binding</a>, you can call <code>this.env.ASSETS.fetch()</code> from within an RPC method. Since RPC methods do not receive a <code>request</code> parameter, construct a <code>Request</code> or URL with any hostname — the hostname is ignored by the assets binding, only the pathname matters:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17248.md")
</div></div>
<p>The caller can then invoke this method via RPC:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17252.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17225.md")
</aside>
<h2 id="named-entrypoints">Named entrypoints</h2>
<p>You can also export any number of named <code>WorkerEntrypoint</code> classes from within a single Worker, in addition to the default export. You can then declare a Service binding to a specific named entrypoint.</p>
<p>You can use this to group multiple pieces of compute together. For example, you might create a distinct <code>WorkerEntrypoint</code> for each permission role in your application, and use these to provide role-specific RPC methods:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17253.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17256.md")
</div></div>
<p>You can then declare a Service binding directly to <code>AdminEntrypoint</code> in another Worker:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17257.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17260.md")
</div></div>
<p>You can learn more about how to configure D1 in the <a href="/d1/get-started/#3-bind-your-worker-to-your-d1-database">D1 documentation</a>.</p>
<p>You can try out a complete example of this to do app, as well as a Discord bot built with named entrypoints, by cloning the <a href="https://github.com/cloudflare/js-rpc-and-entrypoints-demo">cloudflare/js-rpc-and-entrypoints-demo repository</a> from GitHub.</p>
<h2 id="further-reading">Further reading</h2>
<ul class="directory-listing"><li><a href="/workers/runtime-apis/rpc/lifecycle/">Lifecycle</a></li><li><a href="/workers/runtime-apis/rpc/reserved-methods/">Reserved Methods</a></li><li><a href="/workers/runtime-apis/rpc/visibility/">Visibility and Security Model</a></li><li><a href="/workers/runtime-apis/rpc/typescript/">TypeScript</a></li><li><a href="/workers/runtime-apis/rpc/error-handling/">Error handling</a></li></ul>
