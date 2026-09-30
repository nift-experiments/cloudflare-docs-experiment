---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/
  description: Additional load balancing features and integrations.
  full_title: Additional configuration · Cloudflare Load Balancing docs
  head_html: <title>Additional configuration · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Additional load balancing features and integrations."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/index.md"><meta property="og:title" content="Additional configuration · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Additional load balancing features and integrations."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/load-balancing/additional-options/#page","headline":"Additional configuration \u00b7 Cloudflare Load Balancing docs","description":"Additional load balancing features and integrations.","url":"https://developers.cloudflare.com/load-balancing/additional-options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/
  schema: 1
---
<p>Beyond <a href="/load-balancing/load-balancers/create-load-balancer/">creating a simple load balancer</a>, you may want to further customize how your load balancer routes traffic or integrate your load balancer with other Cloudflare products.</p>
<h2 id="customize-load-balancer-behavior">Customize load balancer behavior</h2>
<ul>
<li>Route traffic according to characteristics of each request by <a href="/load-balancing/additional-options/load-balancing-rules/">creating custom rules</a></li>
<li>Protect at-risk endpoints from reaching failover by <a href="/load-balancing/additional-options/load-shedding/">setting up load shedding</a></li>
<li>Take endpoints out of rotation for <a href="/load-balancing/additional-options/planned-maintenance/">planned maintenance</a></li>
<li>Return endpoint hostnames as <code>CNAME</code> records to support downstream DNS steering with <a href="/load-balancing/additional-options/cname-flattening/">CNAME flattening for endpoints</a></li>
</ul>
<h2 id="integrate-with-other-cloudflare-products">Integrate with other Cloudflare products</h2>
<ul>
<li>Bring load balancing to your TCP or UDP applications with <a href="/load-balancing/additional-options/spectrum/">Cloudflare Spectrum</a></li>
<li>Further secure endpoint access with <a href="/load-balancing/additional-options/cloudflare-tunnel/">Cloudflare Tunnel</a></li>
</ul>
<h2 id="integrate-with-3rd-parties">Integrate with 3rd parties</h2>
<ul>
<li>Increase visibility by <a href="/load-balancing/additional-options/pagerduty-integration/">sending health monitor notifications to PagerDuty</a></li>
</ul>
