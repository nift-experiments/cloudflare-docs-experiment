---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/saas/code-deployment/
  description: Let your customers deploy their own code on your platform with isolated execution environments.
  full_title: Enable customer code deployment · Cloudflare use cases
  head_html: <title>Enable customer code deployment · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Let your customers deploy their own code on your platform with isolated execution environments."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/saas/code-deployment/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/saas/code-deployment/index.md"><meta property="og:title" content="Enable customer code deployment · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Let your customers deploy their own code on your platform with isolated execution environments."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/saas/code-deployment/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Workers,R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/saas/code-deployment/#page","headline":"Enable customer code deployment \u00b7 Cloudflare use cases","description":"Let your customers deploy their own code on your platform with isolated execution environments.","url":"https://developers.cloudflare.com/use-cases/saas/code-deployment/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/saas/code-deployment/
  schema: 1
---
<p>SaaS platforms often need to let customers run their own code — custom logic, integrations, webhooks — without compromising tenant isolation or platform stability. Cloudflare Workers for Platforms runs each customer's code in a separate V8 isolate with dispatch routing based on hostname, path, or header.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers-for-platforms">Workers for Platforms</h3>
<p>Deploy isolated Workers execution environments for your customers. <a href="/cloudflare-for-platforms/workers-for-platforms/">Learn more about Workers for Platforms</a>.</p>
<ul>
<li><strong>Tenant isolation</strong> - Each customer's code runs in a separate V8 isolate with no shared memory between tenants</li>
<li><strong>Custom logic</strong> - Customers can deploy their own Workers to extend or customize your platform's behavior</li>
<li><strong>Dispatch routing</strong> - Route incoming requests to the correct customer Worker based on hostname, path, or header</li>
<li><strong>Observability</strong> - Tail Workers capture logs and errors across all tenant code from a single integration</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/get-started/">Workers for Platforms get started</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Configure Dispatch Namespaces</a></li>
</ol>
