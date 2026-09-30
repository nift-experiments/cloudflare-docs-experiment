---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/
  description: The time spent executing a Cloudflare Worker in milliseconds.
  full_title: cf.timings.worker_msec · Cloudflare Ruleset Engine docs
  head_html: <title>cf.timings.worker_msec · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The time spent executing a Cloudflare Worker in milliseconds."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.timings.worker_msec · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The time spent executing a Cloudflare Worker in milliseconds."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/#page","headline":"cf.timings.worker_msec \u00b7 Cloudflare Ruleset Engine docs","description":"The time spent executing a Cloudflare Worker in milliseconds.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/
  schema: 1
---
<h1 id="cf-timings-worker-msec">cf.timings.worker_msec</h1>

**Data type:** Integer

<p>The time spent executing a Cloudflare Worker in milliseconds.</p>

<p>This field provides the wall-clock time that a Cloudflare Worker spent handling the request, measured in milliseconds.</p>
<p>Use this field to identify slow Worker executions, set up alerts for performance regressions, or add Worker execution time as a request header using Transform Rules for downstream observability.</p>
<p>If the request did not invoke a Worker, the value of this field will be <code>0</code>.</p>

**Example value:**

```txt
12
```

**Example usage:**

```txt
# Matches requests where the Worker execution time exceeded 500 milliseconds
cf.timings.worker_msec > 500
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, workers, performance, latency

