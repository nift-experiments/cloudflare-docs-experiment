---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/
  description: Array of string values with the type of unsafe topics detected in the LLM prompt.
  full_title: cf.llm.prompt.unsafe_topic_categories · Cloudflare Ruleset Engine docs
  head_html: <title>cf.llm.prompt.unsafe_topic_categories · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Array of string values with the type of unsafe topics detected in the LLM prompt."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.llm.prompt.unsafe_topic_categories · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Array of string values with the type of unsafe topics detected in the LLM prompt."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/#page","headline":"cf.llm.prompt.unsafe_topic_categories \u00b7 Cloudflare Ruleset Engine docs","description":"Array of string values with the type of unsafe topics detected in the LLM prompt.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/
  schema: 1
---
<h1 id="cf-llm-prompt-unsafe-topic-categories">cf.llm.prompt.unsafe_topic_categories</h1>

**Data type:** Array<String>

<p>Array of string values with the type of unsafe topics detected in the LLM prompt.</p>

<p>The possible values are the following:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Category name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>S1</code></td>
<td>Violent crimes</td>
<td>Violent crimes against people or animals.</td>
</tr>
<tr>
<td><code>S2</code></td>
<td>Non-violent crimes</td>
<td>Non-violent offenses such as fraud, theft, drug creation, or hacking.</td>
</tr>
<tr>
<td><code>S3</code></td>
<td>Sex-related crimes</td>
<td>Sex-related crimes, including trafficking, assault, and harassment.</td>
</tr>
<tr>
<td><code>S4</code></td>
<td>Child sexual exploitation</td>
<td>Sexual exploitation of children.</td>
</tr>
<tr>
<td><code>S5</code></td>
<td>Defamation</td>
<td>False statements that are likely to damage a living person's reputation.</td>
</tr>
<tr>
<td><code>S6</code></td>
<td>Specialized advice</td>
<td>Specialized financial, medical, or legal advice, or misrepresent dangerous things as safe.</td>
</tr>
<tr>
<td><code>S7</code></td>
<td>Privacy</td>
<td>Sensitive, nonpublic personal information that could endanger an individual.</td>
</tr>
<tr>
<td><code>S8</code></td>
<td>Intellectual property</td>
<td>Violate a third party's intellectual property rights.</td>
</tr>
<tr>
<td><code>S9</code></td>
<td>Indiscriminate weapons</td>
<td>Creation of indiscriminate weapons like chemical, biological, or nuclear arms.</td>
</tr>
<tr>
<td><code>S10</code></td>
<td>Hate</td>
<td>Demean or dehumanize people based on their race, religion, sexual orientation, or other personal characteristics.</td>
</tr>
<tr>
<td><code>S11</code></td>
<td>Suicide and self-harm</td>
<td>Encourage or endorse suicide, self-injury, or disordered eating.</td>
</tr>
<tr>
<td><code>S12</code></td>
<td>Sexual content</td>
<td>Erotic content.</td>
</tr>
<tr>
<td><code>S13</code></td>
<td>Elections</td>
<td>False information about the time, place, or manner of voting in elections.</td>
</tr>
<tr>
<td><code>S14</code></td>
<td>Code interpreter abuse</td>
<td>Misuse of code execution capabilities.</td>
</tr>
</tbody>
</table>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where an unsafe topic categorized as "S2" (Non-violent crimes) or "S10" (Hate) was detected in the LLM prompt:
(cf.llm.prompt.unsafe_topic_detected and any(cf.llm.prompt.unsafe_topic_categories[*] in {"S2" "S10"}))
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

