---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/
  description: Replace your VPN with Cloudflare Zero Trust.
  full_title: Get started with Zero Trust · Cloudflare Learning Paths
  head_html: <title>Get started with Zero Trust · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Replace your VPN with Cloudflare Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/index.md"><meta property="og:title" content="Get started with Zero Trust · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Replace your VPN with Cloudflare Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/#page","headline":"Get started with Zero Trust \u00b7 Cloudflare Learning Paths","description":"Replace your VPN with Cloudflare Zero Trust.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/get-started/
  schema: 1
---
<p>In this learning path, you will learn how to replace your existing VPN provider with Cloudflare's ZTNA solution. Your users will run the Cloudflare One Client on their devices, and you will run either Cloudflare Tunnel or Cloudflare Mesh in your network or on your application servers. After deploying Zero Trust, users will be able to connect to private resources (not exposed to the Internet) via TCP/UDP/ICMP, and administrators will be able to control access to these resources based on user identity, device posture, and other factors.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-10.svg" alt="How Cloudflare connects a user device to a private network application" /></p>
<p>This guide will highlight best practices to follow and other decisions to consider when planning your deployment. Additionally, each module will include links to the key resources and how-to pages needed to get your deployment up and running.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9885.md")
</aside>
<h2 id="objectives">Objectives</h2>
<p>By the end of this module, you will be able to:</p>
<ul>
<li>Understand the high-level architecture and requirements for a ZTNA deployment to replace a legacy VPN.</li>
</ul>
<ul>
<li>Set up a Cloudflare account.</li>
<li>Create a Zero Trust organization to manage your devices and policies.</li>
<li>Configure an identity provider (IdP) for user authentication.</li>
</ul>
