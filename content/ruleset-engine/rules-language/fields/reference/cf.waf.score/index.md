---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/
  description: A global score from 1–99 that combines the score of each WAF attack vector into a single score.
  full_title: cf.waf.score · Cloudflare Ruleset Engine docs
  head_html: <title>cf.waf.score · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="A global score from 1–99 that combines the score of each WAF attack vector into a single score."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.waf.score · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A global score from 1–99 that combines the score of each WAF attack vector into a single score."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/#page","headline":"cf.waf.score \u00b7 Cloudflare Ruleset Engine docs","description":"A global score from 1\u201399 that combines the score of each WAF attack vector into a single score.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.waf.score/
  schema: 1
---
<h1 id="cf-waf-score">cf.waf.score</h1>

**Data type:** Number

<p>A global score from 1–99 that combines the score of each WAF attack vector into a single score.</p>

<p>The special score <code>100</code> indicates that Cloudflare did not score the request.</p>
<p>This is the standard <a href="/waf/detections/attack-score/">WAF attack score</a> to detect variants of attack patterns.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/attack-score/">attack score detection</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, attack score, waf score, client, visitor

