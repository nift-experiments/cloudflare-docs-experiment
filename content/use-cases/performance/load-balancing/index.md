---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/performance/load-balancing/
  description: Distribute traffic across multiple servers for reliability and performance.
  full_title: Balance traffic across origins · Cloudflare use cases
  head_html: <title>Balance traffic across origins · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Distribute traffic across multiple servers for reliability and performance."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/performance/load-balancing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/performance/load-balancing/index.md"><meta property="og:title" content="Balance traffic across origins · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Distribute traffic across multiple servers for reliability and performance."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/performance/load-balancing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/performance/load-balancing/#page","headline":"Balance traffic across origins \u00b7 Cloudflare use cases","description":"Distribute traffic across multiple servers for reliability and performance.","url":"https://developers.cloudflare.com/use-cases/performance/load-balancing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/performance/load-balancing/
  schema: 1
---
<p>If a single origin server handles all your traffic, any failure or overload takes your application offline. Cloudflare's load balancing distributes traffic across multiple origins with health checks and automatic failover.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="load-balancing">Load balancing</h3>
<p>Distribute traffic across origins with health checks and failover. <a href="/load-balancing/">Learn more about load balancing</a>.</p>
<ul>
<li><strong>Traffic distribution</strong> - Spread incoming load across multiple origin servers using weighted or latency-based policies</li>
<li><strong>Failover</strong> - Reroute traffic to healthy origins instantly when a server fails its health check</li>
<li><strong>Geographic steering</strong> - Route users to the nearest or best-performing origin based on latency or geography</li>
</ul>
<h3 id="health-checks">Health checks</h3>
<p>Monitor origin server health and availability. <a href="/health-checks/">Learn more about health checks</a>.</p>
<ul>
<li><strong>Health monitoring</strong> - Continuously probe origins and automatically remove unhealthy servers from rotation</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/load-balancing/get-started/">Create a load balancer</a></li>
<li><a href="/health-checks/get-started/">Configure health checks</a></li>
<li><a href="/load-balancing/understand-basics/traffic-steering/">Set up steering policies</a></li>
</ol>
