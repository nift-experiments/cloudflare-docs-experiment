---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/load-balancing/setup/
  description: Distribute traffic across servers with load balancing.
  full_title: Setup · Cloudflare Learning Paths
  head_html: <title>Setup · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Distribute traffic across servers with load balancing."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/load-balancing/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/load-balancing/setup/index.md"><meta property="og:title" content="Setup · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Distribute traffic across servers with load balancing."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/load-balancing/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/load-balancing/setup/#page","headline":"Setup \u00b7 Cloudflare Learning Paths","description":"Distribute traffic across servers with load balancing.","url":"https://developers.cloudflare.com/learning-paths/load-balancing/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/load-balancing/setup/
  schema: 1
---
<p>Create a load balancer that monitors endpoint health and intelligently routes traffic.</p>
<h2 id="objectives">Objectives</h2>
<p>By the end of this module, you will be able to:</p>
<ul>
<li>Configure a monitor and health checks.</li>
<li>Create a pool.</li>
<li>Create a load balancer.</li>
<li>Analyze traffic patterns.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Multiple endpoints, either physical or cloud-based.</li>
<li>Access to Load Balancing, available as an <a href="/load-balancing/get-started/enable-load-balancing/">add-on</a> for any type of account.</li>
<li>Two hostnames, one for test traffic and the other for production traffic.</li>
</ul>
