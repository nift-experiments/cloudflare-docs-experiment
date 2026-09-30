---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/
  description: Indicates whether Cloudflare detected an LLM prompt in the incoming request.
  full_title: cf.llm.prompt.detected · Cloudflare Ruleset Engine docs
  head_html: <title>cf.llm.prompt.detected · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Indicates whether Cloudflare detected an LLM prompt in the incoming request."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.llm.prompt.detected · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Indicates whether Cloudflare detected an LLM prompt in the incoming request."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/#page","headline":"cf.llm.prompt.detected \u00b7 Cloudflare Ruleset Engine docs","description":"Indicates whether Cloudflare detected an LLM prompt in the incoming request.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/
  schema: 1
---
<h1 id="cf-llm-prompt-detected">cf.llm.prompt.detected</h1>

**Data type:** Boolean

<p>Indicates whether Cloudflare detected an LLM prompt in the incoming request.</p>

<p>When a prompt is not present, the other LLM-related fields will have default values.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

