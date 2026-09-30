---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/saas/
  description: Build multi-tenant SaaS platforms with Cloudflare SSL for SaaS, Workers for Platforms, and per-tenant storage.
  full_title: SaaS platforms · Use cases · Cloudflare use cases
  head_html: <title>SaaS platforms · Use cases · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Build multi-tenant SaaS platforms with Cloudflare SSL for SaaS, Workers for Platforms, and per-tenant storage."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/saas/index.md"><meta property="og:title" content="SaaS platforms · Use cases · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build multi-tenant SaaS platforms with Cloudflare SSL for SaaS, Workers for Platforms, and per-tenant storage."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Use cases,Cloudflare for SaaS,Workers,R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/use-cases/saas/#page","headline":"SaaS platforms \u00b7 Use cases \u00b7 Cloudflare use cases","description":"Build multi-tenant SaaS platforms with Cloudflare SSL for SaaS, Workers for Platforms, and per-tenant storage.","url":"https://developers.cloudflare.com/use-cases/saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/saas/
  schema: 1
---
<p>Build multi-tenant platforms with custom domains, isolated compute, and per-customer configuration. Cloudflare SSL for SaaS provisions and renews SSL certificates for every customer hostname. Workers for Platforms runs customer code in isolated V8 environments. D1, KV, and R2 provide per-tenant data storage. Workers Analytics Engine and Logpush track usage for billing and compliance.</p>
<ul class="directory-listing"><li><a href="/use-cases/saas/custom-domains/">Customer domains with SSL for SaaS</a></li><li><a href="/use-cases/saas/code-deployment/">Enable customer code deployment</a></li><li><a href="/use-cases/saas/data-isolation/">Store and isolate customer data</a></li><li><a href="/use-cases/saas/protect-platform/">Protect your platform</a></li><li><a href="/use-cases/saas/usage-analytics/">Observe customer usage and billing</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="custom-domains-with-ssl">Custom domains with SSL</h3>
<p>Allow customers to use their own domains with automatic certificate management:</p>
<ul>
<li><strong>SSL for SaaS</strong> provisions and renews certificates for every custom hostname</li>
<li><strong>Cloudflare for Platforms</strong> routes customer domains to your platform with per-tenant configuration</li>
</ul>
<h3 id="multi-tenant-compute">Multi-tenant compute</h3>
<p>Let customers deploy their own code on your platform:</p>
<ul>
<li><strong>Workers for Platforms</strong> runs customer code in isolated V8 environments</li>
<li><strong>Dispatch namespaces</strong> route requests to the correct tenant Worker based on hostname or path</li>
<li><strong>SSL for SaaS</strong> handles custom domains for each tenant</li>
</ul>
<h3 id="full-multi-tenant-platform">Full multi-tenant platform</h3>
<p>Combine custom domains, tenant compute, and isolated storage:</p>
<ul>
<li><strong>SSL for SaaS</strong> manages customer hostnames and certificates</li>
<li><strong>Workers for Platforms</strong> runs per-tenant application logic</li>
<li><strong>D1</strong> or <strong>KV</strong> stores per-tenant data with database-level or key-prefix isolation</li>
<li><strong>R2</strong> stores per-tenant files and assets</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> for your platform (for example, <code>yourplatform.com</code>). SSL for SaaS uses this as the provider domain against which customer custom hostnames are issued. Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/enable/">Enable Cloudflare for SaaS</a>.</li>
<li>A <a href="/workers/platform/pricing/">Workers Paid plan</a> for Workers for Platforms. Dispatch namespaces, which route requests to customer-specific Workers, are not available on the free tier.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> installed.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> for your platform. This is your domain, not your customers' domains. SSL for SaaS issues customer custom hostnames against this provider domain. Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/enable/">Enable Cloudflare for SaaS</a>.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> if you plan to add Workers for Platforms or manage bindings programmatically.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15224.md")
</div>
