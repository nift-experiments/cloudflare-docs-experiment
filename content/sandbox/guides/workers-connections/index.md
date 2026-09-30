---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/guides/workers-connections/
  description: Access KV, R2, Durable Objects, and other bindings from a sandbox.
  full_title: Connect to Workers bindings · Cloudflare Sandbox SDK docs
  head_html: <title>Connect to Workers bindings · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Access KV, R2, Durable Objects, and other bindings from a sandbox."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/guides/workers-connections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/guides/workers-connections/index.md"><meta property="og:title" content="Connect to Workers bindings · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access KV, R2, Durable Objects, and other bindings from a sandbox."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/guides/workers-connections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK,KV,R2,Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/guides/workers-connections/#page","headline":"Connect to Workers bindings \u00b7 Cloudflare Sandbox SDK docs","description":"Access KV, R2, Durable Objects, and other bindings from a sandbox.","url":"https://developers.cloudflare.com/sandbox/guides/workers-connections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/guides/workers-connections/
  schema: 1
---
<p>Sandboxes can access <a href="/workers/runtime-apis/bindings/">Workers bindings</a> — KV, R2, D1, Durable Objects, and others — through <a href="/sandbox/guides/outbound-traffic/#define-outbound-handlers">outbound handlers</a>. An outbound handler intercepts HTTP requests from the sandbox and runs inside the Workers runtime, where all of your configured bindings are available.</p>
<p>The sandbox makes a plain HTTP request to a virtual hostname (for example, <code>http://my.kv/some-key</code>), and the outbound handler resolves it using the bound resource. No SDK or client library is required inside the sandbox.</p>
<h2 id="use-bindings-in-outbound-handlers">Use bindings in outbound handlers</h2>
<p>Define an <code>outboundByHost</code> handler for each virtual hostname. The <code>env</code> argument gives you access to every binding declared in your Wrangler configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13344.md")
</div>
<p>The sandbox calls <code>http://my.kv/some-key</code> and the handler resolves it using the KV binding. A call to <code>http://my.r2/file.png</code> reads from R2, scoped to the current sandbox instance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13343.md")
</aside>
<h2 id="access-durable-object-state">Access Durable Object state</h2>
<p>The <code>ctx</code> argument exposes <code>containerId</code>, which lets you interact with the sandbox's own Durable Object from an outbound handler.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13345.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a> — Block, allow, and intercept all outbound HTTP from a sandbox</li>
<li><a href="/sandbox/configuration/sandbox-options/">Sandbox options</a> — Configure sandbox behavior</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> — Configure secrets and environment variables</li>
</ul>
