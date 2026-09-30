---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/e-commerce/
  description: Protect and accelerate online stores with Cloudflare WAF, DDoS protection, caching, image optimization, and Waiting Room.
  full_title: E-commerce · Use cases · Cloudflare use cases
  head_html: <title>E-commerce · Use cases · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Protect and accelerate online stores with Cloudflare WAF, DDoS protection, caching, image optimization, and Waiting Room."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/e-commerce/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/e-commerce/index.md"><meta property="og:title" content="E-commerce · Use cases · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect and accelerate online stores with Cloudflare WAF, DDoS protection, caching, image optimization, and Waiting Room."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/e-commerce/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Use cases,WAF,DDoS Protection,Cache / CDN,Cloudflare Images,Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/use-cases/e-commerce/#page","headline":"E-commerce \u00b7 Use cases \u00b7 Cloudflare use cases","description":"Protect and accelerate online stores with Cloudflare WAF, DDoS protection, caching, image optimization, and Waiting Room.","url":"https://developers.cloudflare.com/use-cases/e-commerce/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/e-commerce/
  schema: 1
---
<p>E-commerce applications require exceptional performance, security, and reliability. Cloudflare protects and accelerates online stores with application security against attacks, bot security against credential stuffing and fraud, cache and image optimization for fast global delivery of product pages, load balancing and Waiting Room for handling traffic spikes, and Zaraz for server-side analytics and marketing tags.</p>
<ul class="directory-listing"><li><a href="/use-cases/e-commerce/protect/">Protect your store</a></li><li><a href="/use-cases/e-commerce/performance/">Accelerate your store&#x27;s performance</a></li><li><a href="/use-cases/e-commerce/traffic-at-scale/">Handle traffic at scale</a></li><li><a href="/use-cases/e-commerce/analytics/">Observe traffic patterns and analytics</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="self-hosted-storefront">Self-hosted storefront</h3>
<p>Protect and accelerate a store running on your own infrastructure:</p>
<ul>
<li><strong>SSL/TLS</strong> encrypts all traffic between shoppers and your store</li>
<li><strong>Cache</strong> serves static assets from 300+ edge locations</li>
<li><strong>Application security</strong> blocks attacks before they reach your origin</li>
<li><strong>Images</strong> optimizes product images on-the-fly</li>
</ul>
<h3 id="saas-hosted-storefront">SaaS-hosted storefront</h3>
<p>Add Cloudflare on top of a platform like Shopify, BigCommerce, or Salesforce Commerce Cloud:</p>
<ul>
<li><strong>Cloudflare for SaaS</strong> (Orange-to-Orange setup) layers your Cloudflare zone over your provider's existing Cloudflare configuration</li>
<li><strong>Application security</strong> adds protection beyond what the platform provides</li>
<li><strong>Zaraz</strong> loads analytics and marketing tags server-side to improve page speed</li>
</ul>
<h3 id="high-traffic-store">High-traffic store</h3>
<p>Handle flash sales, seasonal peaks, and viral demand:</p>
<ul>
<li><strong>Load Balancing</strong> distributes traffic across multiple origin servers</li>
<li><strong>Waiting Room</strong> queues excess visitors to prevent origin overload</li>
<li><strong>Cache</strong> and <strong>Argo Smart Routing</strong> reduce origin load and improve response times</li>
<li><strong>Health Checks</strong> detect unhealthy origins and reroute traffic automatically</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare. All solutions in this use case require traffic to pass through Cloudflare's network.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare's network.</li>
<li>If your store is hosted on a SaaS platform that already uses Cloudflare — such as <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/">Shopify</a>, <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/">BigCommerce</a>, or <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/">Salesforce Commerce Cloud</a> — follow the setup steps in the provider guide for your platform to add your own Cloudflare zone on top of your provider's existing configuration.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15235.md")
</div>
