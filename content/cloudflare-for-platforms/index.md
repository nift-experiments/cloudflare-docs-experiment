---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/
  description: Build platforms on Cloudflare where your customers can deploy code with their own subdomains or custom domains.
  full_title: Cloudflare for Platforms · Cloudflare for Platforms docs
  head_html: <title>Cloudflare for Platforms · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Build platforms on Cloudflare where your customers can deploy code with their own subdomains or custom domains."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/index.md"><meta property="og:title" content="Cloudflare for Platforms · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build platforms on Cloudflare where your customers can deploy code with their own subdomains or custom domains."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/#page","headline":"Cloudflare for Platforms \u00b7 Cloudflare for Platforms docs","description":"Build platforms on Cloudflare where your customers can deploy code with their own subdomains or custom domains.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1327.md")
</div>
<p>Cloudflare for Platforms is used by leading platforms big and small to:</p>
<ul>
<li>Build application development platforms tailored to specific domains, like ecommerce storefronts or mobile apps</li>
<li>Power AI coding platforms that let anyone build and deploy software</li>
<li>Customize product behavior by allowing any user to write a short code snippet</li>
<li>Offer every customer their own isolated database</li>
<li>Provide each customer with their own subdomain</li>
</ul>
<hr />
<h2 id="deploy-your-own-platform">Deploy your own platform</h2>
<p>Get a working platform running in minutes. Choose a template based on what you are building:</p>
<h3 id="platform-starter-kit">Platform Starter Kit</h3>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/worker-publisher-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>An example of a platform where users can deploy code at scale. Each snippet becomes its own isolated Worker, served at <code>example.com/{app-name}</code>. Deploying this starter kit automatically configures Workers for Platforms with routing handled for you.</p>
<p><a class="nb-link-button" href="https://worker-publisher-template.templates.workers.dev/">View demo</a>
<a class="nb-link-button" href="https://github.com/cloudflare/templates/tree/main/worker-publisher-template">View on GitHub</a></p>
<h3 id="ai-vibe-coding-platform">AI vibe coding platform</h3>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/vibesdk"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>Build an <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">AI vibe coding platform</a> where users describe what they want and AI generates and deploys working applications. Best for: AI-powered app builders, code generation tools, or internal platforms that empower teams to build applications &amp; prototypes.</p>
<p><a href="https://github.com/cloudflare/vibesdk">VibeSDK</a> handles AI code generation, code execution in secure sandboxes, live previews, and deployment at scale.</p>
<p><a class="nb-link-button" href="https://build.cloudflare.dev/">View demo</a>
<a class="nb-link-button" href="https://github.com/cloudflare/vibesdk">View on GitHub</a></p>
<hr />
<h2 id="features">Features</h2>
<ul>
<li><strong>Isolation and multitenancy</strong> — Each of your customers runs code in their own Worker, a <a href="/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/">secure and isolated sandbox</a>.</li>
<li><strong>Programmable routing, ingress, egress, and limits</strong> — You write code that dispatches requests to your customers' code, and can control <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">ingress</a>, <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">egress</a>, and set <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/">per-customer limits</a>.</li>
<li><strong>Databases and storage</strong> — You can provide <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">databases, object storage, and more</a> to your customers as APIs they can call directly, without API tokens, keys, or external dependencies.</li>
<li><strong>Custom domains and subdomains</strong> — You <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">call an API</a> to create custom subdomains or configure custom domains for each of your customers.</li>
</ul>
<p>To learn how these components work together, refer to <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/">How Workers for Platforms works</a>.</p>
