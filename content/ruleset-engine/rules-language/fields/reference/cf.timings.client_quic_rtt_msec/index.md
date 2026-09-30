---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/
  description: The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.
  full_title: cf.timings.client_quic_rtt_msec · Cloudflare Ruleset Engine docs
  head_html: <title>cf.timings.client_quic_rtt_msec · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.timings.client_quic_rtt_msec · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/#page","headline":"cf.timings.client_quic_rtt_msec \u00b7 Cloudflare Ruleset Engine docs","description":"The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/
  schema: 1
---
<h1 id="cf-timings-client-quic-rtt-msec">cf.timings.client_quic_rtt_msec</h1>

**Data type:** Integer

<p>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.</p>

<p>This field is only populated for QUIC (HTTP/3) connections. For TCP connections, the value is <code>0</code>.</p>

**Example value:**

```txt
42
```

**Example usage:**

```txt
# Match requests over QUIC where the RTT exceeds 200 ms
cf.timings.client_quic_rtt_msec > 200
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, quic, rtt, performance, latency, http3

