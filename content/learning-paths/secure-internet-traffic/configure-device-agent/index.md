---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/
  description: Secure Internet traffic and SaaS apps.
  full_title: Configure the device agent · Cloudflare Learning Paths
  head_html: <title>Configure the device agent · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Secure Internet traffic and SaaS apps."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/index.md"><meta property="og:title" content="Configure the device agent · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Secure Internet traffic and SaaS apps."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/#page","headline":"Configure the device agent \u00b7 Cloudflare Learning Paths","description":"Secure Internet traffic and SaaS apps.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/configure-device-agent/
  schema: 1
---
<p>The Cloudflare One Client (known as the Cloudflare One Agent in mobile app stores) encrypts designated traffic from a user's device to Cloudflare's global network. In this learning path, we will first define all of your parameters and deployment rules, and then we will install and connect the client. If you prefer to start the client download now, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Download the Cloudflare One Client</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10081.md")
</aside>
<h2 id="objectives">Objectives</h2>
<p>By the end of this module, you will be able to:</p>
<ul>
<li>Define which users can connect devices to your Zero Trust instance.</li>
<li>Configure global and device-specific settings for the Cloudflare One Client.</li>
<li>Route user traffic through Cloudflare Gateway.</li>
<li>Route domains to a private DNS server, if required.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshoot-the-cloudflare-one-client">Troubleshoot the Cloudflare One Client</h3>
@markup("md", "content/.markup/bodies/10080.md")
</aside>
