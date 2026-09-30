---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/platform/limits/
  description: Resource limits for Sandbox SDK including vCPU, memory, disk, and container constraints.
  full_title: Limits · Cloudflare Sandbox SDK docs
  head_html: <title>Limits · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Resource limits for Sandbox SDK including vCPU, memory, disk, and container constraints."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resource limits for Sandbox SDK including vCPU, memory, disk, and container constraints."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Sandbox SDK docs","description":"Resource limits for Sandbox SDK including vCPU, memory, disk, and container constraints.","url":"https://developers.cloudflare.com/sandbox/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/platform/limits/
  schema: 1
---
<p>Since the Sandbox SDK is built on top of the <a href="/containers/">Containers</a> platform, it shares the same underlying platform characteristics. Refer to these pages to understand how pricing and limits work for your sandbox deployments.</p>
<p>Sandbox also inherits current Containers lifecycle, placement, and routing behavior. For more
detail, refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a> and
<a href="/containers/configuration/scaling-and-routing/">Scaling and Routing</a>.</p>
<h2 id="container-limits">Container limits</h2>
<p>Refer to <a href="/containers/platform/limits/">Containers limits</a> for complete details on:</p>
<ul>
<li>Memory, vCPU, and disk limits for concurrent container instances</li>
<li>Instance types and their resource allocations</li>
<li>Image size and storage limits</li>
</ul>
<h2 id="workers-and-durable-objects-limits">Workers and Durable Objects limits</h2>
<p>When using the Sandbox SDK from Workers or Durable Objects, you are subject to <a href="/workers/platform/limits/#subrequests">Workers subrequest limits</a>. By default, the SDK uses HTTP transport where each operation (<code>exec()</code>, <code>readFile()</code>, <code>writeFile()</code>, etc.) counts as one subrequest.</p>
<h3 id="subrequest-limits">Subrequest limits</h3>
<ul>
<li><strong>Workers Free</strong>: 50 subrequests per request</li>
<li><strong>Workers Paid</strong>: 1,000 subrequests per request</li>
</ul>
<h3 id="avoid-subrequest-limits-with-rpc-transport">Avoid subrequest limits with RPC transport</h3>
<p>Enable RPC transport to multiplex all SDK calls over a single persistent connection:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13342.md")
</div>
<p>With RPC transport enabled:</p>
<ul>
<li>The persistent connection counts as one subrequest</li>
<li>All subsequent SDK operations use the existing connection (no additional subrequests)</li>
<li>Ideal for workflows with many SDK operations per request</li>
</ul>
<p>See <a href="/sandbox/configuration/transport/">Transport modes</a> for a complete guide.</p>
<h2 id="best-practices">Best practices</h2>
<p>To work within these limits:</p>
<ul>
<li><strong>Right-size your instances</strong> - Choose the appropriate <a href="/containers/platform/limits/#instance-types">instance type</a> based on your workload requirements</li>
<li><strong>Clean up unused sandboxes</strong> - Terminate sandbox sessions when they are no longer needed to free up resources</li>
<li><strong>Optimize images</strong> - Keep your <a href="/sandbox/configuration/dockerfile/">custom Dockerfiles</a> lean to reduce image size</li>
<li><strong>Use RPC transport for high-frequency operations</strong> - Enable <code>SANDBOX_TRANSPORT=rpc</code> to avoid subrequest limits when making many SDK calls per request</li>
</ul>
