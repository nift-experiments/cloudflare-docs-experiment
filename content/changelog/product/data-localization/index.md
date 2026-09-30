---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/data-localization/
  description: '2026-06-23'
  full_title: data-localization changelog | Cloudflare Docs
  head_html: <title>data-localization changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-23"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/data-localization/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="data-localization changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-23"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/data-localization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/data-localization/#page","headline":"data-localization changelog | Cloudflare Docs","description":"2026-06-23","url":"https://developers.cloudflare.com/changelog/product/data-localization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/data-localization/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>



