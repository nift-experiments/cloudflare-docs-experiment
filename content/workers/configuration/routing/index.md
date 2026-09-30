---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/routing/
  description: Connect your Worker to an external endpoint (via Routes, Custom Domains or a `workers.dev` subdomain) such that it can be accessed by the Internet.
  full_title: Routes and domains · Cloudflare Workers docs
  head_html: <title>Routes and domains · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect your Worker to an external endpoint (via Routes, Custom Domains or a `workers.dev` subdomain) such that it can be accessed by the Internet."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/routing/index.md"><meta property="og:title" content="Routes and domains · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect your Worker to an external endpoint (via Routes, Custom Domains or a `workers.dev` subdomain) such that it can be accessed by the Internet."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/configuration/routing/#page","headline":"Routes and domains \u00b7 Cloudflare Workers docs","description":"Connect your Worker to an external endpoint (via Routes, Custom Domains or a workers.dev subdomain) such that it can be accessed by the Internet.","url":"https://developers.cloudflare.com/workers/configuration/routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/routing/
  schema: 1
---
<p>To allow a Worker to receive inbound HTTP requests, you must connect it to an external endpoint such that it can be accessed by the Internet.</p>
<p>There are three types of routes:</p>
<ul>
<li>
<p><a href="/workers/configuration/routing/custom-domains">Custom Domains</a>: Routes to a domain or subdomain (such as <code>example.com</code> or <code>shop.example.com</code>) within a Cloudflare zone where the Worker is the origin.</p>
</li>
<li>
<p><a href="/workers/configuration/routing/routes/">Routes</a>: Routes that are set within a Cloudflare zone where your origin server, if you have one, is behind a Worker that the Worker can communicate with.</p>
</li>
<li>
<p><a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a>: A <code>workers.dev</code> subdomain route is automatically created for each Worker to help you getting started quickly. You may choose to <a href="/workers/configuration/routing/workers-dev/">disable</a> your <code>workers.dev</code> subdomain.</p>
</li>
</ul>
<h2 id="what-is-best-for-me">What is best for me?</h2>
<p>It's recommended to run production Workers on a <a href="/workers/configuration/routing/">Workers route or custom domain</a>, rather than on your <code>workers.dev</code> subdomain. Your <code>workers.dev</code> subdomain is treated as a <a href="https://www.cloudflare.com/plans/">Free website</a> and is intended for personal or hobby projects that aren't business-critical.</p>
<p>Custom Domains are recommended for use cases where your Worker is your application's origin server. Custom Domains can also be invoked within the same zone via <code>fetch()</code>, unlike Routes.</p>
<p>Routes are recommended for use cases where your application's origin server is external to Cloudflare. Note that Routes cannot be the target of a same-zone <code>fetch()</code> call.</p>
