---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/
  description: The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per RFC 9440.
  full_title: cf.tls_client_auth.cert_chain_rfc9440 · Cloudflare Ruleset Engine docs
  head_html: <title>cf.tls_client_auth.cert_chain_rfc9440 · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per RFC 9440."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.tls_client_auth.cert_chain_rfc9440 · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per RFC 9440."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/#page","headline":"cf.tls_client_auth.cert_chain_rfc9440 \u00b7 Cloudflare Ruleset Engine docs","description":"The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per RFC 9440.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/
  schema: 1
---
<h1 id="cf-tls-client-auth-cert-chain-rfc9440">cf.tls_client_auth.cert_chain_rfc9440</h1>

**Data type:** String

<p>The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per <a href="https://datatracker.ietf.org/doc/html/rfc9440">RFC 9440</a>.</p>

<p>Contains the DER-encoded, Base64-wrapped client certificate chain formatted as an <a href="https://datatracker.ietf.org/doc/html/rfc9440#name-client-cert-chain-http-head">RFC 9440</a> <code>Client-Cert-Chain</code> HTTP header value. The value is a structured field list of byte sequences. The leaf certificate is not included in the chain (it is available in <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/"><code>cf.tls_client_auth.cert_rfc9440</code></a>). The chain reflects the certificates as sent by the client, without any reordering or validation.</p>
<p>This field is populated regardless of the certificate validation result. Before using this value, verify the certificate status by checking <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/"><code>cf.tls_client_auth.cert_verified</code></a> and <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/"><code>cf.tls_client_auth.cert_revoked</code></a>.</p>
<p>Returns <code>&quot;&quot;</code> if the client did not send any intermediate certificates or if the encoded value exceeds the 16 KiB size limit. Refer to <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/"><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></a> to distinguish between these cases.</p>
<p>This field defaults to <code>&quot;&quot;</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

**Example value:**

```txt
":MII.....=:, :MII....=:"
```

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor, rfc9440, cert, chain

