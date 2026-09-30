---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/
  description: Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.
  full_title: cf.llm.prompt.pii_categories · Cloudflare Ruleset Engine docs
  head_html: <title>cf.llm.prompt.pii_categories · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.llm.prompt.pii_categories · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/#page","headline":"cf.llm.prompt.pii_categories \u00b7 Cloudflare Ruleset Engine docs","description":"Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/
  schema: 1
---
<h1 id="cf-llm-prompt-pii-categories">cf.llm.prompt.pii_categories</h1>

**Data type:** Array<String>

<p>Array of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.</p>

<p>The possible values are the following:</p>
<table>
<thead>
<tr>
<th>Category</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>BANK_ACCOUNT</code></td>
<td>Bank account number</td>
</tr>
<tr>
<td><code>CREDIT_CARD</code></td>
<td>Credit card number</td>
</tr>
<tr>
<td><code>DATE_TIME</code></td>
<td>Date or time expression</td>
</tr>
<tr>
<td><code>DRIVER_LICENSE</code></td>
<td>Driver license number</td>
</tr>
<tr>
<td><code>EMAIL_ADDRESS</code></td>
<td>Email address</td>
</tr>
<tr>
<td><code>IP_ADDRESS</code></td>
<td>Internet Protocol (IPv4) address</td>
</tr>
<tr>
<td><code>LOCATION</code></td>
<td>Physical location or address</td>
</tr>
<tr>
<td><code>PASSPORT</code></td>
<td>Passport number</td>
</tr>
<tr>
<td><code>PERSON</code></td>
<td>Full or partial name of an individual</td>
</tr>
<tr>
<td><code>PHONE_NUMBER</code></td>
<td>Telephone number</td>
</tr>
<tr>
<td><code>TAX_ID</code></td>
<td>Tax identification number</td>
</tr>
<tr>
<td><code>US_SSN</code></td>
<td>US Social Security Number (SSN)</td>
</tr>
<tr>
<td><code>URL</code></td>
<td>Uniform Resource Locator (URL), used to locate a resource on the Internet</td>
</tr>
</tbody>
</table>
<p>The categories are detected by an AI-based Named Entity Recognition (NER) model.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where PII categorized as "EMAIL_ADDRESS" or "BANK_ACCOUNT" was detected:
(cf.llm.prompt.pii_detected and any(cf.llm.prompt.pii_categories[*] in {"EMAIL_ADDRESS" "BANK_ACCOUNT"}))
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

