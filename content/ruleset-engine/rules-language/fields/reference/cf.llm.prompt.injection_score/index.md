---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/
  description: A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.
  full_title: cf.llm.prompt.injection_score · Cloudflare Ruleset Engine docs
  head_html: <title>cf.llm.prompt.injection_score · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.llm.prompt.injection_score · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/#page","headline":"cf.llm.prompt.injection_score \u00b7 Cloudflare Ruleset Engine docs","description":"A score from 1\u201399 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/
  schema: 1
---
<h1 id="cf-llm-prompt-injection-score">cf.llm.prompt.injection_score</h1>

**Data type:** Number

<p>A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.</p>

<p>A low score (for example, below <code>20</code>) indicates that there is a high probability that the LLM prompt in the request is trying to perform a prompt injection attack.</p>
<p>The special score <code>100</code> indicates that Cloudflare did not score the request.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

