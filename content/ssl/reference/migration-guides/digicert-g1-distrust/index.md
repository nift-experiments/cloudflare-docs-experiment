---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-g1-distrust/
  description: Learn how the DigiCert G1 root distrust may affect your Cloudflare configuration.
  full_title: DigiCert Legacy Root (G1) distrust by major browsers · Cloudflare SSL/TLS docs
  head_html: <title>DigiCert Legacy Root (G1) distrust by major browsers · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how the DigiCert G1 root distrust may affect your Cloudflare configuration."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-g1-distrust/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-g1-distrust/index.md"><meta property="og:title" content="DigiCert Legacy Root (G1) distrust by major browsers · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how the DigiCert G1 root distrust may affect your Cloudflare configuration."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-g1-distrust/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-g1-distrust/#page","headline":"DigiCert Legacy Root (G1) distrust by major browsers \u00b7 Cloudflare SSL/TLS docs","description":"Learn how the DigiCert G1 root distrust may affect your Cloudflare configuration.","url":"https://developers.cloudflare.com/ssl/reference/migration-guides/digicert-g1-distrust/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/migration-guides/digicert-g1-distrust/
  schema: 1
---
<p>Browsers and operating systems are completing the removal of DigiCert's legacy G1 root certificates from their trust stores, effective <strong>April 15, 2026</strong>.</p>
<p>DigiCert announced this planned deprecation in 2023 and has been issuing certificates from their newer G2 roots since 2020.</p>
<p>Since DigiCert is not within the <a href="/ssl/reference/certificate-authorities/">certificate authorities</a> used by Cloudflare, this change may only affect customers who upload <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a> issued from DigiCert G1 roots.</p>
<h2 id="the-change">The change</h2>
<p>The primary root being distrusted is <strong>DigiCert Global Root CA</strong>. The distrust also affects other legacy G1 intermediates cross-signed from this root.</p>
<p>DigiCert Global Root G2 and G3 remain fully trusted. Certificates that chain to G2 are unaffected.</p>
<p>Refer to <a href="https://knowledge.digicert.com/general-information/digicert-root-and-intermediate-ca-certificate-updates-2023">DigiCert's root and intermediate CA certificate updates</a> for the full list of affected roots.</p>
<h2 id="digicert-s-recommendation">DigiCert's recommendation</h2>
<p>DigiCert recommends reissuing any affected certificates from a G2 intermediate. This is a standard reissuance — you do not need to generate a new key in most cases.</p>
<h2 id="cloudflare-managed-certificates">Cloudflare-managed certificates</h2>
<p>Since Cloudflare does not use DigiCert roots, you can avoid this dependency entirely by switching to Cloudflare-managed certificates:</p>
<ul>
<li>Use <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificates</a> for more control and flexibility with automatic renewals.</li>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> to automatically issue certificates for your <a href="/dns/proxy-status/">proxied hostnames</a>.</li>
<li>Use <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a> to reduce manual intervention when renewing certificates for <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setup</a> zones.</li>
</ul>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="https://knowledge.digicert.com/general-information/digicert-root-and-intermediate-ca-certificate-updates-2023">DigiCert root and intermediate CA certificate updates</a></li>
<li><a href="/ssl/edge-certificates/custom-certificates/">Custom certificates</a></li>
<li><a href="/ssl/edge-certificates/custom-certificates/bundling-methodologies/">Certificate bundling methodologies</a></li>
</ul>
