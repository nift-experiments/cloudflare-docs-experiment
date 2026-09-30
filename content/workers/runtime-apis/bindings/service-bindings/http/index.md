---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/
  description: Facilitate Worker-to-Worker communication by forwarding Request objects.
  full_title: Service bindings - HTTP · Cloudflare Workers docs
  head_html: <title>Service bindings - HTTP · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Facilitate Worker-to-Worker communication by forwarding Request objects."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/index.md"><meta property="og:title" content="Service bindings - HTTP · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Facilitate Worker-to-Worker communication by forwarding Request objects."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/#page","headline":"Service bindings - HTTP \u00b7 Cloudflare Workers docs","description":"Facilitate Worker-to-Worker communication by forwarding Request objects.","url":"https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/bindings/service-bindings/http/
  schema: 1
---
<p>Worker A that declares a Service binding to Worker B can forward a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object to Worker B, by calling the <code>fetch()</code> method that is exposed on the binding object.</p>
<p>For example, consider the following Worker that implements a <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17267.md")
</div>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(&quot;Hello World!&quot;);&#10;  }&#10;}&#10;</code></pre>
<p>The following Worker declares a binding to the Worker above:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17268.md")
</div>
<p>And then can forward a request to it:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		return await env.WORKER_B.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17266.md")
</aside>
