---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/
  description: An array of file sizes in bytes, in the order the content objects were detected in the request.
  full_title: cf.waf.content_scan.obj_sizes · Cloudflare Ruleset Engine docs
  head_html: <title>cf.waf.content_scan.obj_sizes · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="An array of file sizes in bytes, in the order the content objects were detected in the request."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.waf.content_scan.obj_sizes · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="An array of file sizes in bytes, in the order the content objects were detected in the request."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/#page","headline":"cf.waf.content_scan.obj_sizes \u00b7 Cloudflare Ruleset Engine docs","description":"An array of file sizes in bytes, in the order the content objects were detected in the request.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/
  schema: 1
---
<h1 id="cf-waf-content-scan-obj-sizes">cf.waf.content_scan.obj_sizes</h1>

**Data type:** Array<Integer>

<p>An array of file sizes in bytes, in the order the content objects were detected in the request.</p>

<p>Requires a Cloudflare Enterprise plan with <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a>.</p>

**Example usage:**

```txt
# Check if requests to a specific endpoint contain any content objects larger than 500 KB (512,000 bytes)
any(cf.waf.content_scan.obj_sizes[*] > 512000) and http.request.uri.path eq "/upload"
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, content scanning, malicious uploads, client, visitor

