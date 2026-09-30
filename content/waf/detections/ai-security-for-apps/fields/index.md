---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/
  description: Fields available for AI Security for Apps detections in rule expressions.
  full_title: AI Security for Apps fields · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>AI Security for Apps fields · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Fields available for AI Security for Apps detections in rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/index.md"><meta property="og:title" content="AI Security for Apps fields · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fields available for AI Security for Apps detections in rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/#page","headline":"AI Security for Apps fields \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Fields available for AI Security for Apps detections in rule expressions.","url":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/ai-security-for-apps/fields/
  schema: 1
---
<p>When enabled, AI Security for Apps populates the following fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>LLM PII detected <br/> [<code>cf.llm.prompt.pii_detected</code>][1] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request.</td>
</tr>
<tr>
<td>LLM PII categories <br/> [<code>cf.llm.prompt.pii_categories</code>][2] <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.<br/><a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/">Category list</a></td>
</tr>
<tr>
<td>LLM Content detected <br/> [<code>cf.llm.prompt.detected</code>][3] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether Cloudflare detected an LLM prompt in the incoming request.</td>
</tr>
<tr>
<td>LLM Unsafe topic detected <br/> [<code>cf.llm.prompt.unsafe_topic_detected</code>][4] <br/> <span class="nb-type">Boolean</span></td>
<td>Indicates whether the incoming request includes any unsafe topic category in the LLM prompt.</td>
</tr>
<tr>
<td>LLM Unsafe topic categories <br/> [<code>cf.llm.prompt.unsafe_topic_categories</code>][5] <br/> <span class="nb-type">Array&lt;String&gt;</span></td>
<td>Array of string values with the type of unsafe topics detected in the LLM prompt.<br/><a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/">Category list</a></td>
</tr>
<tr>
<td>LLM Injection score <br/> [<code>cf.llm.prompt.injection_score</code>][6] <br/> <span class="nb-type">Number</span></td>
<td>A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack. Lower scores indicate higher risk.</td>
</tr>
<tr>
<td>LLM Token count <br/> [<code>cf.llm.prompt.token_count</code>][7] <br/> <span class="nb-type">Number</span></td>
<td>An estimated token count for the LLM prompt in the request. Refer to <a href="/waf/detections/ai-security-for-apps/token-counting/">Token counting</a> for details.</td>
</tr>
<tr>
<td>LLM Custom topic categories <br/> [<code>cf.llm.prompt.custom_topic_categories</code>][8] <br/> <span class="nb-type">Map&lt;Number&gt;</span></td>
<td>A map of custom topic labels to relevance scores (1–99). Lower scores indicate the prompt is more relevant to that topic. Only populated when <a href="/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics">custom topics</a> are configured.</td>
</tr>
</tbody>
</table>
