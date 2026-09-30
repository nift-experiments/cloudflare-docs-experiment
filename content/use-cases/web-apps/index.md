---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/web-apps/
  description: Build and deploy full-stack web applications on Cloudflare with Workers, D1, KV, R2, Durable Objects, and Queues.
  full_title: Web sites and web apps · Use cases · Cloudflare use cases
  head_html: <title>Web sites and web apps · Use cases · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Build and deploy full-stack web applications on Cloudflare with Workers, D1, KV, R2, Durable Objects, and Queues."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/web-apps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/web-apps/index.md"><meta property="og:title" content="Web sites and web apps · Use cases · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build and deploy full-stack web applications on Cloudflare with Workers, D1, KV, R2, Durable Objects, and Queues."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/web-apps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Use cases,Workers,R2,D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/use-cases/web-apps/#page","headline":"Web sites and web apps \u00b7 Use cases \u00b7 Cloudflare use cases","description":"Build and deploy full-stack web applications on Cloudflare with Workers, D1, KV, R2, Durable Objects, and Queues.","url":"https://developers.cloudflare.com/use-cases/web-apps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/web-apps/
  schema: 1
---
<p>Build and deploy full-stack web applications globally with serverless compute, storage, and instant deployments. Cloudflare Workers runs your frontend and backend logic at the edge. D1 provides a serverless SQL database. KV stores key-value data globally. R2 provides S3-compatible object storage with zero egress fees. Durable Objects coordinates real-time state. Queues handles background processing.</p>
<ul class="directory-listing"><li><a href="/use-cases/web-apps/deploy-frontend/">Deploy frontend applications</a></li><li><a href="/use-cases/web-apps/serverless-backends/">Build serverless backends</a></li><li><a href="/use-cases/web-apps/store-data/">Store application data</a></li><li><a href="/use-cases/web-apps/real-time/">Add real-time features</a></li><li><a href="/use-cases/web-apps/performance/">Optimize performance</a></li><li><a href="/use-cases/web-apps/security/">Secure your application</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="full-stack-application">Full-stack application</h3>
<p>Build a complete application with frontend and backend:</p>
<ul>
<li><strong>Workers</strong> serves your frontend assets (React, Vue, Astro, and similar frameworks) and handles Application Programming Interface (API) routes</li>
<li><strong>D1</strong> stores application data</li>
<li><strong>R2</strong> stores user uploads and assets</li>
</ul>
<h3 id="real-time-collaborative-app">Real-time collaborative app</h3>
<p>Build multiplayer or collaborative features:</p>
<ul>
<li><strong>Durable Objects</strong> coordinates state and WebSocket connections</li>
<li><strong>Workers</strong> handles HTTP requests and routing</li>
<li><strong>KV</strong> caches frequently accessed data</li>
<li><strong>Queues</strong> processes background tasks</li>
</ul>
<h3 id="static-site-with-dynamic-features">Static site with dynamic features</h3>
<p>Add interactivity to static content:</p>
<ul>
<li><strong>Workers</strong> serves static HTML/CSS/JavaScript (JS) and handles form submissions and API calls</li>
<li><strong>KV</strong> stores form data and user preferences</li>
<li><strong>R2</strong> stores uploaded files</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) installed on your machine.</li>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> installed. Wrangler is the CLI for creating, testing, and deploying Workers projects.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare. This is required for security features (SSL/TLS, Application security), caching, and performance optimizations.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> if you plan to add Workers-based functionality to your existing application.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15086.md")
</div>
