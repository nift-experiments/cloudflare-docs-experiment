---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/
  description: Upgrade your Keyless SSL key server to the latest version.
  full_title: Upgrade your key server · Cloudflare SSL/TLS docs
  head_html: <title>Upgrade your key server · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Upgrade your Keyless SSL key server to the latest version."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/index.md"><meta property="og:title" content="Upgrade your key server · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upgrade your Keyless SSL key server to the latest version."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/#page","headline":"Upgrade your key server \u00b7 Cloudflare SSL/TLS docs","description":"Upgrade your Keyless SSL key server to the latest version.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/upgrading-your-key-server/
  schema: 1
---
<p>Periodically, you may need to update your key server when using Cloudflare's Keyless SSL.</p>
<p>To upgrade your key server:</p>
<ol>
<li>Back up the contents of <code>/etc/keyless</code>.</li>
<li>Update your OS’ package listings, for example, <code>apt-get update</code> or <code>yum update</code>.</li>
<li>Upgrade the gokeyless server:</li>
<li>Debian/Ubuntu: <code>apt-get upgrade gokeyless</code></li>
<li>RHEL/CentOS: <code>yum install gokeyless</code></li>
<li>Restart the keyless instance:</li>
<li>systemd: <code>service gokeyless restart</code></li>
<li>upstart/sysvinit: <code>/etc/init.d/gokeyless restart</code></li>
<li>Confirm that HTTPS connections are working as expected.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14002.md")
</aside>
