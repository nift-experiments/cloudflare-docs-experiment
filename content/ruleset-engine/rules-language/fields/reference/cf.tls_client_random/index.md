---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/
  description: The value of the 32-byte random value provided by the client in a TLS handshake, encoded in Base64.
  full_title: cf.tls_client_random · Cloudflare Ruleset Engine docs
  head_html: <title>cf.tls_client_random · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The value of the 32-byte random value provided by the client in a TLS handshake, encoded in Base64."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.tls_client_random · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The value of the 32-byte random value provided by the client in a TLS handshake, encoded in Base64."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/#page","headline":"cf.tls_client_random \u00b7 Cloudflare Ruleset Engine docs","description":"The value of the 32-byte random value provided by the client in a TLS handshake, encoded in Base64.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.tls_client_random/
  schema: 1
---
<h1 id="cf-tls-client-random">cf.tls_client_random</h1>

**Data type:** String

<p>The value of the 32-byte random value provided by the client in a <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake">TLS handshake</a>, encoded in Base64.</p>

<p>For more details, refer to <a href="https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2">RFC 8446</a>.</p>

**Example value:**

```txt
"YWJjZA=="
```

<h2 id="categories">Categories</h2>

- Request
- SSL/TLS

**Keywords:** request, ssl, tls, client, visitor

