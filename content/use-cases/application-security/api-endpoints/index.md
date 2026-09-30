---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/application-security/api-endpoints/
  description: Protect APIs with schema validation, rate limiting, and authentication.
  full_title: Secure API endpoints · Cloudflare use cases
  head_html: <title>Secure API endpoints · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Protect APIs with schema validation, rate limiting, and authentication."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/application-security/api-endpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/application-security/api-endpoints/index.md"><meta property="og:title" content="Secure API endpoints · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Protect APIs with schema validation, rate limiting, and authentication."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/application-security/api-endpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,API Shield,SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/application-security/api-endpoints/#page","headline":"Secure API endpoints \u00b7 Cloudflare use cases","description":"Protect APIs with schema validation, rate limiting, and authentication.","url":"https://developers.cloudflare.com/use-cases/application-security/api-endpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/application-security/api-endpoints/
  schema: 1
---
<p>API endpoints are vulnerable to schema violations, abuse, and unauthorized access. Cloudflare API Shield validates requests against your OpenAPI specification, and mutual TLS (mTLS) authenticates known clients with certificates.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="api-shield">API Shield</h3>
<p>Discover, secure, and monitor your APIs. <a href="/api-shield/">Learn more about API Shield</a>.</p>
<ul>
<li><strong>API discovery</strong> - Automatically identify API endpoints in your traffic, including undocumented ones</li>
<li><strong>Schema validation</strong> - Reject requests that do not conform to your OpenAPI specification</li>
<li><strong>Sequence mitigation</strong> - Detect and block API abuse patterns such as out-of-order requests</li>
</ul>
<h3 id="mtls">mTLS</h3>
<p>Mutual TLS client certificate authentication. <a href="/ssl/client-certificates/">Learn more about mTLS</a>.</p>
<ul>
<li><strong>mTLS authentication</strong> - Require client certificates for machine-to-machine API access</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/api-shield/get-started/">API Shield get started</a></li>
<li><a href="/ssl/client-certificates/">Set up mTLS</a></li>
</ol>
