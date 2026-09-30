---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/
  description: Store private keys in hardware security modules for Keyless SSL.
  full_title: Hardware security modules · Cloudflare SSL/TLS docs
  head_html: <title>Hardware security modules · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Store private keys in hardware security modules for Keyless SSL."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/index.md"><meta property="og:title" content="Hardware security modules · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store private keys in hardware security modules for Keyless SSL."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/#page","headline":"Hardware security modules \u00b7 Cloudflare SSL/TLS docs","description":"Store private keys in hardware security modules for Keyless SSL.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/hardware-security-modules/
  schema: 1
---
<p>In addition to private keys stored on disk, Keyless SSL supports keys stored in a Hardware Security Module (HSM) via the PKCS#11 standard. Keyless uses PKCS#11 for signing and decrypting payloads without having direct access to the private keys.</p>
<hr />
<h2 id="why-use-keyless-ssl-with-an-hsm">Why use Keyless SSL with an HSM?</h2>
<p>Hardware Security Modules (HSMs) facilitate a higher level of protection for your private keys over storing them directly on your key server. The primary responsibility of an HSM is safeguarding private keys and performing operations such as signing or encryption internally. In addition to access control, that means the physical device must offer some degree of tamper-resistance in order to be compliant with government or <a href="https://csrc.nist.gov/pubs/fips/140-3/final">industry regulations such as FIPS 140</a>.</p>
<p>Moreover, many HSMs are also capable of generating keys and producing cryptographically secure randomness. Some are purpose-built to perform cryptographic computations more efficiently.</p>
<hr />
<h2 id="communicating-using-pkcs-11">Communicating using PKCS#11</h2>
<p>The key server communicates with HSMs via PKCS#11, so any HSM supporting the standard can be used with Keyless SSL.</p>
<h3 id="initial-configuration">Initial configuration</h3>
<p>For more details on initializing your PKCS#11 token, refer to <a href="/ssl/keyless-ssl/hardware-security-modules/configuration/">Configuration</a>.</p>
<h3 id="compatibility">Compatibility</h3>
<p>Keyless SSL has interoperability with the following modules:</p>
<ul>
<li><a href="https://www.entrust.com/digital-security/hsm">Entrust nShield Connect</a></li>
<li><a href="https://cpl.thalesgroup.com/compliance/fips-common-criteria-validations">Gemalto SafeNet Luna</a></li>
<li><a href="https://github.com/opendnssec/SoftHSMv2">SoftHSMv2</a></li>
<li><a href="https://www.yubico.com/product/yubikey-neo/">YubiKey Neo</a></li>
</ul>
<p>Also, the following cloud HSM offerings have been tested with Keyless SSL:</p>
<ul>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/">AWS CloudHSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/azure-dedicated-hsm/">Azure Dedicated HSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/azure-managed-hsm/">Azure Managed HSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/">Fortanix DSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/">IBM Cloud HSM</a></li>
<li><a href="/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/">Google Cloud HSM</a></li>
</ul>
