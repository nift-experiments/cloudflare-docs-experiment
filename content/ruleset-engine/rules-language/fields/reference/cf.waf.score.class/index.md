---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/
  description: The attack score class of the current request, based on the WAF attack score.
  full_title: cf.waf.score.class · Cloudflare Ruleset Engine docs
  head_html: <title>cf.waf.score.class · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The attack score class of the current request, based on the WAF attack score."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.waf.score.class · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The attack score class of the current request, based on the WAF attack score."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/#page","headline":"cf.waf.score.class \u00b7 Cloudflare Ruleset Engine docs","description":"The attack score class of the current request, based on the WAF attack score.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.waf.score.class/
  schema: 1
---
<h1 id="cf-waf-score-class">cf.waf.score.class</h1>

**Data type:** String

<p>The attack score class of the current request, based on the WAF attack score.</p>

<p>Can have one of the following values: <code>attack</code>, <code>likely_attack</code>, <code>likely_clean</code>, <code>clean</code>.</p>
<p>Requires a Cloudflare Business plan or above. You must also enable <a href="/waf/detections/attack-score/">attack score detection</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, attack score, waf score, client, visitor

