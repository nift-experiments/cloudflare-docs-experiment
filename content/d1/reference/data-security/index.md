---
cp9:
  canonical: https://developers.cloudflare.com/d1/reference/data-security/
  description: D1 encrypts data at rest and in transit, and is covered by Cloudflare's SOC 2 and ISO 27001 compliance certifications.
  full_title: Data security · Cloudflare D1 docs
  head_html: <title>Data security · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="D1 encrypts data at rest and in transit, and is covered by Cloudflare&#x27;s SOC 2 and ISO 27001 compliance certifications."><link rel="canonical" href="https://developers.cloudflare.com/d1/reference/data-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/reference/data-security/index.md"><meta property="og:title" content="Data security · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="D1 encrypts data at rest and in transit, and is covered by Cloudflare&#x27;s SOC 2 and ISO 27001 compliance certifications."><meta property="og:url" content="https://developers.cloudflare.com/d1/reference/data-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/reference/data-security/#page","headline":"Data security \u00b7 Cloudflare D1 docs","description":"D1 encrypts data at rest and in transit, and is covered by Cloudflare's SOC 2 and ISO 27001 compliance certifications.","url":"https://developers.cloudflare.com/d1/reference/data-security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/reference/data-security/
  schema: 1
---
<p>This page details the data security properties of D1, including:</p>
<ul>
<li>Encryption-at-rest (EAR).</li>
<li>Encryption-in-transit (EIT).</li>
<li>Cloudflare's compliance certifications.</li>
</ul>
<h2 id="encryption-at-rest">Encryption at Rest</h2>
<p>All objects stored in D1, including metadata, live databases, and inactive databases are encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of D1.</p>
<p>Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.</p>
<p>Objects are encrypted using <a href="https://www.cloudflare.com/learning/ssl/what-is-encryption/">AES-256</a>, a widely tested, highly performant and industry-standard encryption algorithm. D1 uses GCM (Galois/Counter Mode) as its preferred mode.</p>
<h2 id="encryption-in-transit">Encryption in Transit</h2>
<p>Data transfer between a Cloudflare Worker, and/or between nodes within the Cloudflare network and D1 is secured using the same <a href="https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/">Transport Layer Security</a> (TLS/SSL).</p>
<p>API access via the HTTP API or using the <a href="/workers/wrangler/install-and-update/">wrangler</a> command-line interface is also over TLS/SSL (HTTPS).</p>
<h2 id="compliance">Compliance</h2>
<p>To learn more about Cloudflare's adherence to industry-standard security compliance certifications, visit the Cloudflare <a href="https://www.cloudflare.com/trust-hub/compliance-resources/">Trust Hub</a>.</p>
