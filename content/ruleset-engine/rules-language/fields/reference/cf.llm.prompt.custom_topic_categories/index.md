---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/
  description: A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.
  full_title: cf.llm.prompt.custom_topic_categories · Cloudflare Ruleset Engine docs
  head_html: <title>cf.llm.prompt.custom_topic_categories · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.llm.prompt.custom_topic_categories · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/#page","headline":"cf.llm.prompt.custom_topic_categories \u00b7 Cloudflare Ruleset Engine docs","description":"A map of custom topic labels to relevance scores (1\u201399) for the LLM prompt in the request.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/
  schema: 1
---
<h1 id="cf-llm-prompt-custom-topic-categories">cf.llm.prompt.custom_topic_categories</h1>

**Data type:** Map<Number>

<p>A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.</p>

<p>Lower scores indicate the prompt is more relevant to that topic. Only populated when <a href="/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics">custom topics</a> are configured.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where the prompt is highly relevant to the "competitors" custom topic:
(cf.llm.prompt.custom_topic_categories["competitors"] lt 30)
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

