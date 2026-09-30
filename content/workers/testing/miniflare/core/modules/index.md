---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/core/modules/
  description: 'Miniflare supports both the traditional service-worker and the newer modules formats for writing workers. To use the modules format, enable it with:'
  full_title: Modules · Cloudflare Workers docs
  head_html: <title>Modules · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Miniflare supports both the traditional service-worker and the newer modules formats for writing workers. To use the modules format, enable it with:"><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/core/modules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/core/modules/index.md"><meta property="og:title" content="Modules · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Miniflare supports both the traditional service-worker and the newer modules formats for writing workers. To use the modules format, enable it with:"><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/core/modules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/miniflare/core/modules/#page","headline":"Modules \u00b7 Cloudflare Workers docs","description":"Miniflare supports both the traditional service-worker and the newer modules formats for writing workers. To use the modules format, enable it with:","url":"https://developers.cloudflare.com/workers/testing/miniflare/core/modules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/core/modules/
  schema: 1
---
<ul>
<li><a href="/workers/reference/migrate-to-module-workers/">Modules Reference</a></li>
</ul>
<h2 id="enabling-modules">Enabling Modules</h2>
<p>Miniflare supports both the traditional <code>service-worker</code> and the newer <code>modules</code> formats for writing workers. To use the <code>modules</code> format, enable it with:</p>
<pre tabindex="0"><code class="language-js">const mf = new Miniflare({&#10;	modules: true,&#10;});&#10;</code></pre>
<p>You can then use <code>modules</code> worker scripts like the following:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// - `request` is the incoming `Request` instance&#10;		// - `env` contains bindings, KV namespaces, Durable Objects, etc&#10;		// - `ctx` contains `waitUntil` and `passThroughOnException` methods&#10;		return new Response(&quot;Hello Miniflare!&quot;);&#10;	},&#10;	async scheduled(controller, env, ctx) {&#10;		// - `controller` contains `scheduledTime` and `cron` properties&#10;		// - `env` contains bindings, KV namespaces, Durable Objects, etc&#10;		// - `ctx` contains the `waitUntil` method&#10;		console.log(&quot;Doing something scheduled...&quot;);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside warning">
@markup("md", "content/.markup/bodies/17366.md")
</aside>
<h2 id="module-rules">Module Rules</h2>
<p>Miniflare supports all module types: <code>ESModule</code>, <code>CommonJS</code>, <code>Text</code>, <code>Data</code> and
<code>CompiledWasm</code>. You can specify additional module resolution rules as follows:</p>
<pre tabindex="0"><code class="language-js">const mf = new Miniflare({&#10;	modulesRules: [&#10;		{ type: &quot;ESModule&quot;, include: [&quot;**/*.js&quot;], fallthrough: true },&#10;		{ type: &quot;Text&quot;, include: [&quot;**/*.txt&quot;] },&#10;	],&#10;});&#10;</code></pre>
<h3 id="default-rules">Default Rules</h3>
<p>The following rules are automatically added to the end of your modules rules
list. You can override them by specifying rules matching the same <code>globs</code>:</p>
<pre tabindex="0"><code class="language-js">[&#10;	{ type: &quot;ESModule&quot;, include: [&quot;**/*.mjs&quot;] },&#10;	{ type: &quot;CommonJS&quot;, include: [&quot;**/*.js&quot;, &quot;**/*.cjs&quot;] },&#10;];&#10;</code></pre>
