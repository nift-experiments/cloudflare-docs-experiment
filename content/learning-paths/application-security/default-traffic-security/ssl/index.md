---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/
  description: Configure SSL/TLS encryption options for domains.
  full_title: SSL / TLS · Cloudflare Learning Paths
  head_html: <title>SSL / TLS · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Configure SSL/TLS encryption options for domains."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/index.md"><meta property="og:title" content="SSL / TLS · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure SSL/TLS encryption options for domains."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF,DDoS Protection,SSL/TLS,DNS,Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/#page","headline":"SSL / TLS \u00b7 Cloudflare Learning Paths","description":"Configure SSL/TLS encryption options for domains.","url":"https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/application-security/default-traffic-security/ssl/
  schema: 1
---
<p>Cloudflare offers a range of SSL/TLS options. By default, Cloudflare offers Universal SSL to all domains, but there are many other options available. Cloudflare offers SSL/TLS for free because we believe it is the <a href="https://blog.cloudflare.com/introducing-universal-ssl">right thing to do</a>. Encryption is foundational to the Internet because it prevents data from being manipulated.</p>
<ol>
<li>
<p><a href="/ssl/edge-certificates/universal-ssl/"><strong>Universal SSL</strong></a>: This option covers basic encryption requirements and certificate management needs.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/additional-options/total-tls/"><strong>Total TLS</strong></a>: Automatically issues certificates for all subdomain levels, extending the protection offered by Universal SSL.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/advanced-certificate-manager/"><strong>Advanced Certificates</strong></a>: Offers customizable certificate issuance and management, including options like choosing the certificate authority, certificate validity period, and removing Cloudflare branding from certificates.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/custom-certificates/"><strong>Custom Certificates</strong></a>: For eligible plans, customers can upload their own certificates, with the user managing issuance and renewal.</p>
</li>
<li>
<p><a href="/ssl/client-certificates/"><strong>mTLS Client Certificates</strong></a>: Cloudflare offers a PKI system, used to create client certificates, which can enforce mutual Transport Layer Security (mTLS) encryption.</p>
</li>
<li>
<p><a href="/cloudflare-for-platforms/cloudflare-for-saas/"><strong>Cloudflare for SaaS Custom Hostnames</strong></a>: This feature enables SaaS providers to offer their clients the ability to use their own domains while benefiting from Cloudflare's network.</p>
</li>
<li>
<p><a href="/ssl/keyless-ssl/"><strong>Keyless SSL Certificates</strong></a>: Keyless SSL allows security-conscious clients to upload their own custom certificates and benefit from Cloudflare, but without exposing their TLS private keys.</p>
</li>
<li>
<p><a href="/ssl/origin-configuration/origin-ca/"><strong>Origin Certificates</strong></a>: Origin CA certificates from Cloudflare are used to encrypt traffic between Cloudflare and your origin web server. These certificates are created through the Cloudflare dashboard and can be configured with a choice of RSA or ECC private keys and support for various server types.</p>
</li>
</ol>
