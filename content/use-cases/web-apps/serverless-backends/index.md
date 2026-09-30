---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/web-apps/serverless-backends/
  description: Deploy backend code globally with automatic scaling, fast startup times, and scheduled tasks.
  full_title: Build serverless backends · Cloudflare use cases
  head_html: <title>Build serverless backends · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Deploy backend code globally with automatic scaling, fast startup times, and scheduled tasks."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/web-apps/serverless-backends/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/web-apps/serverless-backends/index.md"><meta property="og:title" content="Build serverless backends · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy backend code globally with automatic scaling, fast startup times, and scheduled tasks."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/web-apps/serverless-backends/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Workers,Queues,Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/web-apps/serverless-backends/#page","headline":"Build serverless backends \u00b7 Cloudflare use cases","description":"Deploy backend code globally with automatic scaling, fast startup times, and scheduled tasks.","url":"https://developers.cloudflare.com/use-cases/web-apps/serverless-backends/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/web-apps/serverless-backends/
  schema: 1
---
<p>Running backend code on traditional servers requires provisioning capacity, managing scaling, and accepting cold starts. Cloudflare Workers runs your server-side code at the edge with fast startup, automatic scaling, and global distribution across 300+ locations.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>Global deployment</strong> - Code runs at the Cloudflare location nearest to each user automatically</li>
<li><strong>Fast startup</strong> - V8 isolates start in milliseconds with no warm-up period, avoiding the cold start delays of container-based platforms</li>
<li><strong>Auto-scaling</strong> - Handle traffic spikes without provisioning or configuration</li>
</ul>
<h3 id="cron-triggers">Cron Triggers</h3>
<p>Schedule Workers to run on a recurring basis. <a href="/workers/configuration/cron-triggers/">Learn more about Cron Triggers</a>.</p>
<ul>
<li><strong>Scheduled tasks</strong> - Run Workers on a fixed schedule for background jobs and periodic tasks</li>
</ul>
<h3 id="queues">Queues</h3>
<p>Reliable message queuing and background processing for Workers. <a href="/queues/">Learn more about Queues</a>.</p>
<ul>
<li><strong>Async processing</strong> - Reliably process background jobs and webhooks without blocking request handling</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/workers/get-started/">Workers get started</a></li>
<li><a href="/workers/configuration/cron-triggers/">Configure Cron Triggers</a></li>
<li><a href="/queues/get-started/">Queues get started</a></li>
</ol>
