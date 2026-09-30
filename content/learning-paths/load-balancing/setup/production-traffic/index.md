---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/
  description: Learn about route production traffic in this guide.
  full_title: Route production traffic · Cloudflare Learning Paths
  head_html: <title>Route production traffic · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about route production traffic in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/index.md"><meta property="og:title" content="Route production traffic · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about route production traffic in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/#page","headline":"Route production traffic \u00b7 Cloudflare Learning Paths","description":"Learn about route production traffic in this guide.","url":"https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/load-balancing/setup/production-traffic/
  schema: 1
---
<p>Now that you have set up your load balancer and verified everything is working correctly, you can put the load balancer on a live domain or subdomain:</p>
<ol>
<li>If you update your pools and monitors, review the pool health again to make sure everything is working as expected.</li>
<li>Confirm that your production hostname has the correct <a href="/load-balancing/load-balancers/dns-records/#priority-order">priority order</a> of DNS records and is covered by an <a href="/load-balancing/load-balancers/dns-records/#ssltls-coverage">SSL/TLS certificate</a>.</li>
<li>Configure your load balancer to receive production traffic, which could involve either:
<ul>
<li>Editing the <strong>Hostname</strong> of your existing load balancer.</li>
<li>Updating the <code>CNAME</code> record sending traffic to your load balancer.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9798.md")
</aside>
