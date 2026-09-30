---
cp9:
  canonical: https://developers.cloudflare.com/key-transparency/
  description: Secure public key distribution in end-to-end encrypted messaging systems.
  full_title: Overview · Cloudflare Key Transparency Auditor docs
  head_html: <title>Overview · Cloudflare Key Transparency Auditor docs</title><meta name="generator" content="Nift"><meta name="description" content="Secure public key distribution in end-to-end encrypted messaging systems."><link rel="canonical" href="https://developers.cloudflare.com/key-transparency/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/key-transparency/index.md"><meta property="og:title" content="Overview · Cloudflare Key Transparency Auditor docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Secure public key distribution in end-to-end encrypted messaging systems."><meta property="og:url" content="https://developers.cloudflare.com/key-transparency/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Key Transparency Auditor"><meta name="algolia_product_filter" content="Key Transparency Auditor"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Key Transparency Auditor"><meta name="pcx_tags" content="Privacy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/key-transparency/#page","headline":"Overview \u00b7 Cloudflare Key Transparency Auditor docs","description":"Secure public key distribution in end-to-end encrypted messaging systems.","url":"https://developers.cloudflare.com/key-transparency/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy"]}</script>
  markdown: true
  noindex: false
  route: /key-transparency/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/923.md")
</div>
<p>Cloudflare's Key Transparency Auditor aims to secure the distribution of public keys for end-to-end encrypted (E2EE) messaging systems like <a href="https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/">WhatsApp</a>. It achieves this by building a verifiable append-only data structure called a Log, similar to <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Certificate_Transparency">Certificate Transparency</a>.</p>
<p>Cloudflare acts as an auditor of Key Transparency Logs to ensure the transparency of end-to-end encrypted messaging public keys. Cloudflare provides an API for anyone to monitor the verification work we perform, and verify the state of its associated Logs locally.</p>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/924.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/925.md")
</div>
