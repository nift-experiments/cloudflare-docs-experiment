---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/
  description: DNSKEY records used by the 1.1.1.1 resolver.
  full_title: Supported DNSKEY signature algorithms · Cloudflare 1.1.1.1 docs
  head_html: <title>Supported DNSKEY signature algorithms · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="DNSKEY records used by the 1.1.1.1 resolver."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/index.md"><meta property="og:title" content="Supported DNSKEY signature algorithms · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DNSKEY records used by the 1.1.1.1 resolver."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/#page","headline":"Supported DNSKEY signature algorithms \u00b7 Cloudflare 1.1.1.1 docs","description":"DNSKEY records used by the 1.1.1.1 resolver.","url":"https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/encryption/dnskey/
  schema: 1
---
<p>Standard DNS has no built-in way to verify that a response actually came from the authoritative server for a domain. An attacker could return a forged answer, and a resolver would have no way to detect it.</p>
<p><a href="https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/">DNSSEC</a> solves this by adding cryptographic signatures to DNS records. Domain owners sign their DNS records with a private key, and resolvers like 1.1.1.1 verify those signatures using the corresponding public key. This proves the response is authentic and has not been modified in transit.</p>
<p>DNSSEC uses two DNS record types to distribute the public keys needed for verification:</p>
<ul>
<li><strong>DNSKEY</strong> records contain the public signing keys for a domain.</li>
<li><strong>DS</strong> (Delegation Signer) records link a child zone's keys to its parent zone, creating a chain of trust.</li>
</ul>
<p>Resolvers use these keys to verify the signatures stored in <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">RRSIG records</a>.</p>
<h2 id="supported-signature-algorithms">Supported signature algorithms</h2>
<p>1.1.1.1 supports the following DNSSEC signature algorithms:</p>
<ul>
<li>RSA/SHA-1</li>
<li>RSA/SHA-256</li>
<li>RSA/SHA-512</li>
<li>RSASHA1-NSEC3-SHA1</li>
<li>ECDSA Curve P-256 with SHA-256 (ECDSAP256SHA256)</li>
<li>ECDSA Curve P-384 with SHA-384 (ECDSAP384SHA384)</li>
<li>ED25519</li>
</ul>
