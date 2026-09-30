---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/
  description: Contains the specific code for 1XXX Cloudflare errors.
  full_title: cf.response.1xxx_code · Cloudflare Ruleset Engine docs
  head_html: <title>cf.response.1xxx_code · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Contains the specific code for 1XXX Cloudflare errors."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.response.1xxx_code · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Contains the specific code for 1XXX Cloudflare errors."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/#page","headline":"cf.response.1xxx_code \u00b7 Cloudflare Ruleset Engine docs","description":"Contains the specific code for 1XXX Cloudflare errors.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/
  schema: 1
---
<h1 id="cf-response-1xxx-code">cf.response.1xxx_code</h1>

**Data type:** Integer

<p>Contains the specific code for 1XXX Cloudflare errors.</p>

<p>Use this field to differentiate between 1XXX errors associated with the same HTTP status code. The default value is <code>0</code>.</p>
<p>For a list of 1XXX errors, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Troubleshooting Cloudflare 1XXX errors</a>.</p>
<p><strong>Note</strong>: This field is only available in <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> and <a href="/rules/custom-errors/">Custom Errors</a>.</p>

**Example value:**

```txt
1020
```

<h2 id="categories">Categories</h2>

- Response

**Keywords:** response, cloudflare

