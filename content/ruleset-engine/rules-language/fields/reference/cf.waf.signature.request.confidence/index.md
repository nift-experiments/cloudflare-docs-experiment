---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/
  description: An array of confidence values associated with attack signatures that matched the request.
  full_title: cf.waf.signature.request.confidence · Cloudflare Ruleset Engine docs
  head_html: <title>cf.waf.signature.request.confidence · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="An array of confidence values associated with attack signatures that matched the request."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.waf.signature.request.confidence · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="An array of confidence values associated with attack signatures that matched the request."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/#page","headline":"cf.waf.signature.request.confidence \u00b7 Cloudflare Ruleset Engine docs","description":"An array of confidence values associated with attack signatures that matched the request.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/
  schema: 1
---
<h1 id="cf-waf-signature-request-confidence">cf.waf.signature.request.confidence</h1>

**Data type:** Array<String>

<p>An array of confidence values associated with attack signatures that matched the request.</p>

<p>Supported values are <code>high</code> and <code>low</code>.</p>
<p>Available to customers with <a href="/waf/detections/attack-signature-detection/">Attack Signature Detection</a> in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.</p>

**Example value:**

```txt
["high"]
```

**Example usage:**

```txt
any(cf.waf.signature.request.confidence[*] eq "high")
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, waf, attack signature, confidence

