---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/
  description: The most recent data delivery rate estimate for the client connection, in bytes per second.
  full_title: cf.edge.l4.delivery_rate · Cloudflare Ruleset Engine docs
  head_html: <title>cf.edge.l4.delivery_rate · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The most recent data delivery rate estimate for the client connection, in bytes per second."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.edge.l4.delivery_rate · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The most recent data delivery rate estimate for the client connection, in bytes per second."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/#page","headline":"cf.edge.l4.delivery_rate \u00b7 Cloudflare Ruleset Engine docs","description":"The most recent data delivery rate estimate for the client connection, in bytes per second.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/
  schema: 1
---
<h1 id="cf-edge-l4-delivery-rate">cf.edge.l4.delivery_rate</h1>

**Data type:** Integer

<p>The most recent data delivery rate estimate for the client connection, in bytes per second.</p>

<p>This metric reflects the rate at which data is being successfully delivered over the connection.</p>
<p>Returns <code>0</code> when L4 statistics are not available for the request.</p>

**Example value:**

```txt
123456
```

**Example usage:**

```txt
# Match requests where the delivery rate is below 100 KB/s
cf.edge.l4.delivery_rate < 100000
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, l4, delivery rate, bandwidth, network, performance, transport

