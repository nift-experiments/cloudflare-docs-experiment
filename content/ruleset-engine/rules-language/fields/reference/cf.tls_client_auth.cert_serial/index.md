---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/
  description: Serial number of the mTLS client certificate.
  full_title: cf.tls_client_auth.cert_serial · Cloudflare Ruleset Engine docs
  head_html: <title>cf.tls_client_auth.cert_serial · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Serial number of the mTLS client certificate."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.tls_client_auth.cert_serial · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serial number of the mTLS client certificate."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/#page","headline":"cf.tls_client_auth.cert_serial \u00b7 Cloudflare Ruleset Engine docs","description":"Serial number of the mTLS client certificate.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/
  schema: 1
---
<h1 id="cf-tls-client-auth-cert-serial">cf.tls_client_auth.cert_serial</h1>

**Data type:** String

<p>Serial number of the mTLS client certificate.</p>

<p>This field defaults to <code>&quot;&quot;</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

**Example value:**

```txt
"527E0F20A20EA2A4146C78390F34CE7AF0878CA4"
```

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor

